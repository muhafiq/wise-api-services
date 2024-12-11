from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users import User
import json
from app.api.schemas.users import UserSchema
from app.extentions import db
from app.api.error import ResponseError
from datetime import datetime
from app.services.mailer import send_email
from app.utils.token import generate_token, validate_token
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash

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

        updatable_fields = ['name', 'email']
        update_data = {key: value for key, value in validated_data.items() if key in updatable_fields}

        if not update_data:
            raise ResponseError(code=400, description="No valid fields to update")

        update_data["updated_at"] = datetime.now() 
        updated_rows = User.query.filter_by(id=user_id).update(update_data)
        if updated_rows == 0:
            raise ResponseError(code=404, description="User not found")

        db.session.commit()

        updated_user = User.query.filter_by(id=user_id).first()
        
        return {
            "status_code": 200,
            "message": "User profile updated successfully",
            "data": schema.dump(updated_user)
        }, 200

# user mengirimkan email -> email valid? send unique token ke email -> user memasukan token -> reset password

class ForgotPasswordResource(Resource):
    def post(self):

        if not request.json:
            raise ResponseError(code=400, description="Payload cannot be empty!")

        email = request.json.get('email')
        if not email:
            raise ResponseError(code=400, description="Email is required!")
        
        db_user = User.query.filter_by(email=email).first()
        if not db_user:
            raise ResponseError(code=404, description="User not found")
        
        token = generate_token()
        db_user.token = token
        db.session.commit()

        send_email("Reset Password From Wise. Inc", {"email": email, "token": token.split('-')[0]})

        return {
            "status_code": 200,
            "message": "Email sent successfully, please check your email!"
        }, 200

class VerifyTokenResource(Resource):
    def post(self):
        if not request.json:
            raise ResponseError(code=400, description="Payload cannot be empty!")

        email = request.json.get('email')
        if not email:
            raise ResponseError(code=400, description="Email is required!")
        
        token = request.json.get('token')
        if not token:
            raise ResponseError(code=400, description="Token is required!")
        
        db_user = User.query.filter_by(email=email).first()
        if not db_user:
            raise ResponseError(code=404, description="Email not found!")
        
        is_token_valid = validate_token(db_user.token)

        if not is_token_valid:
            raise ResponseError(code=400, description="Token has expired!")

        if type(is_token_valid) == str:
            raise ResponseError(code=400, description=is_token_valid)
        
        return {
            "status_code": 200,
            "message": "Token is valid!"
        }, 200
        

class ResetPasswordResource(Resource):
    def post(self):
        if not request.json:
            raise ResponseError(code=400, description="Payload cannot be empty!")

        schema = UserSchema(partial=True)
        schema.context = {'action': 'reset-password'}

        data = schema.load(request.json)

        db_user = User.query.filter_by(email=data['email']).first()
        if not db_user:
            raise ResponseError(code=404, description="User not found")
        
        is_token_valid = validate_token(db_user.token)

        if not is_token_valid:
            raise ResponseError(code=400, description="Token has expired!")

        if type(is_token_valid) == str:
            raise ResponseError(code=400, description=is_token_valid)
        
        db_user.password = generate_password_hash(data['password'])
        db_user.token = None
        db.session.commit()

        return {
            "status_code": 200,
            "message": "Password reset successfully"
        }, 200