from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.medical_records import MedicalRecord
from app.api.schemas.medical_records import MedicalRecordSchema
from app.api.error import ResponseError
import json

class AllHistoryResource(Resource):
    @jwt_required()
    def get(self):
        schema = MedicalRecordSchema(many=True)
        user_id = json.loads(get_jwt_identity())['id']

        print(user_id)

        medical_records = MedicalRecord.query.filter_by(user_id=user_id)

        return {
            "status_code": 200,
            "message": "Get all medical records successfully",
            "data": schema.dump(medical_records)
        }, 200

class SingleHistoryResource(Resource):
    @jwt_required()
    def get(self, history_id: str):
        schema = MedicalRecordSchema()
        user_id = json.loads(get_jwt_identity())['id']

        medical_record = MedicalRecord.query.filter_by(id=history_id).filter_by(user_id=user_id).first()

        if not medical_record:
            raise ResponseError(code=404, description=f'Medical record with id {history_id} not found')

        return {
            "status_code": 200,
            "message": "Get medical record successfully",
            "data": schema.dump(medical_record)
        }, 200