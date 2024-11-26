from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
import json
from app.api.schemas.users import UserSchema
from app.extentions import db
from app.api.error import ResponseError
from datetime import datetime

class UserResource(Resource):
    @jwt_required()
    def get(self):
        schema = UserSchema()
        schema.context = {"action": "get profile"}
        user_id = json.loads(get_jwt_identity())['id']

        db_user = User.query.filter_by(id=user_id).first()

        if not db_user:
           raise ResponseError(code=404, description="User not found")

        return {
            "status_code": 200,
            "message": "Get user profile successfully",
            "data": schema.dump(db_user)
        }, 200

    @jwt_required()
    def put(self):

        if not request.json:
            raise ResponseError(code=400, description="Payload cannot be empty!")

        schema = UserSchema(partial=True)
        schema.context = {"action": "update profile"}
        user_id = json.loads(get_jwt_identity())['id']

        validated_data = schema.load(request.json)

        db_user = User.query.filter_by(id=user_id).first()

        if not db_user:
           raise ResponseError(code=404, description="User not found")

        updatable_fields = ['name', 'email']  # user can only update listed fields
        for field, value in validated_data.items():
            if field in updatable_fields:
                setattr(db_user, field, value)
        
        db_user.updated_at = datetime.now()

        db.session.commit()

        return {
            "status_code": 200,
            "message": "User profile updated successfully",
            "data": schema.dump(db_user)
        }, 200