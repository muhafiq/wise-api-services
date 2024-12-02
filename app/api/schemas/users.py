from app.extentions import ma
from marshmallow.fields import String, DateTime
from marshmallow import validate, validates_schema, ValidationError
from app.models.users import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    id = String(required=True, validate=[validate.Length(min=36)])
    email = String(required=True, validate=[validate.Email()])
    name = String(required=True, validate=[validate.Length(max=120)])
    no_hp = String(
        required=True, 
        validate=[
            validate.Length(max=16),
            validate.Regexp(r'^\d+$', error="Phone number must contain only digits.")
        ])
    password = String(required=True, validate=[validate.Length(min=8, max=40)])
    confirm_password = String(required=False, validate=[validate.Length(min=8, max=40)])
    address = String(required=False)
    created_at = DateTime()
    updated_at = DateTime()


    @validates_schema
    def validate_confirm_password(self, data, **kwargs):
        if self.context.get("action") == "register":
            if data.get("password") != data.get("confirm_password"):
                raise ValidationError({"confirm_password": ["Password and confirm password must match."]})
        
    @validates_schema
    def validate_unique_email(self, data, **kwargs):
        if self.context.get("action") == "register":
            if User.query.filter_by(email=data.get("email")).count():
                raise ValidationError({"email": ["Email already exist."]})
    
    @validates_schema
    def validate_required_data(self, data, **kwargs):
        if self.context.get("action") == "register":
            required_fields = ["name", "email", "no_hp", "password", "confirm_password"]
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                raise ValidationError({field: ["This field is required."] for field in missing_fields})
        
        elif self.context.get("action") == "login":
            required_fields = ["email", "password"]
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                raise ValidationError({field: ["This field is required."] for field in missing_fields})