from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.api.error import ResponseError
from app.utils.hospital import get_hospital_details

class HospitalResource(Resource):
    @jwt_required()
    def get(self):
        lat = request.args.get('lat')
        lon = request.args.get('lon')

        if not lat or not lon:
            raise ResponseError(code=400, description="Latitude and longitude are required.")

        status, data_hospitals = get_hospital_details(lat, lon)
        if not status:
            raise ResponseError(code=data_hospitals.get('code'), description=data_hospitals.get('message'))

        return {
            "status_code": 200,
            "message": "Get the nearest hospital successfully",
            "data": data_hospitals
        }, 200