from app.extentions import ma
from marshmallow import fields

class MedicalRecordSchema(ma.SQLAlchemyAutoSchema):
    id = fields.String() 
    photo_date = fields.DateTime() 
    diagnosis_id = fields.String() 
    treatment = fields.String() 
    photo = fields.String() 
    created_at = fields.DateTime() 
    updated_at = fields.DateTime() 