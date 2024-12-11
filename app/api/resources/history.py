from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.medical_records import MedicalRecord
from app.api.schemas.medical_records import MedicalRecordSchema, CreateMedicalRecordSchema
from app.api.error import ResponseError
import json
from app.utils.gcs import delete_image_by_url
from flask import request
from app.models.medical_records import MedicalRecord
from datetime import datetime
from app.extentions import db

class AllHistoryResource(Resource):
    @jwt_required()
    def get(self):
        schema = MedicalRecordSchema(many=True, partial=True)
        user_id = json.loads(get_jwt_identity())['id']

        medical_records = MedicalRecord.query.filter_by(user_id=user_id)

        return {
            "status_code": 200,
            "message": "Get all medical records successfully",
            "data": schema.dump(medical_records)
        }, 200

    @jwt_required()
    def post(self):
        schema = CreateMedicalRecordSchema()

        user_id = json.loads(get_jwt_identity())['id']

        if not request.json:
            raise ResponseError(code=400, description="Payload cannot be empty!")

        validated_data = schema.load(request.json)

        validated_data["photo_date"] = datetime.now()
        validated_data["user_id"] = user_id

        medical_record = MedicalRecord(**validated_data)
        db.session.add(medical_record)
        db.session.commit()
        db.session.refresh(medical_record)

        return {
            'status_code': 200,
            'message': 'Add medical record successfully',
            'data': MedicalRecordSchema().dump(medical_record)
        }, 200


class SingleHistoryResource(Resource):
    @jwt_required()
    def get(self, history_id: str):
        schema = MedicalRecordSchema(partial=True)
        user_id = json.loads(get_jwt_identity())['id']

        medical_record = MedicalRecord.query.filter_by(id=history_id).filter_by(user_id=user_id).first()

        if not medical_record:
            raise ResponseError(code=404, description=f'Medical record with id {history_id} not found')

        return {
            "status_code": 200,
            "message": "Get medical record successfully",
            "data": schema.dump(medical_record)
        }, 200

class CancelAddHistoryRecord(Resource):
    def delete(self):
        
        image_url = request.json["photo"]

        if not request.json:
            raise ResponseError(code=400, description="Payload cannot be empty!")

        if not image_url:
            raise ResponseError(code=400, description="No photo url provided!")
        
        message, status = delete_image_by_url(image_url)

        return {
            'status_code': 200,
            'message': message
        }, 200
            