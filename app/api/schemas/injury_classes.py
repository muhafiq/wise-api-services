from app.extentions import ma
from marshmallow import fields

class InjuryClassSchema(ma.SQLAlchemyAutoSchema):
    id = fields.String(dump_only=True)  
    class_name = fields.String(dump_only=True)  
    treatment = fields.String(dump_only=True)  
    created_at = fields.DateTime(dump_only=True)  
    updated_at = fields.DateTime(dump_only=True)  