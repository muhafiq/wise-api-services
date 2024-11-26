from flask import request, abort
from flask_restful import Resource
from app.api.schemas.users import UserSchema
from app.models.users import User
from app.extentions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from app.api.error import ResponseError
import json
from app.models.token_blacklist import TokenBlacklist

class RegisterResource(Resource):
    def post(self):
        schema = UserSchema(partial=True)
        schema.context = {"action": "register"}
        validated_data = schema.load(request.json)

        validated_data.pop("confirm_password", None)
        validated_data["password"] = generate_password_hash(validated_data["password"])

        user = User(**validated_data)
        db.session.add(user)
        db.session.commit()

        return {
            "status_code": 201,
            "message": "User created.",
            "data": {
                "id": user.id
            }
        }, 201

class LoginResource(Resource):
    def post(self):
        schema = UserSchema(partial=True)
        schema.context = {"action": "login"}
        validated_data = schema.load(request.json)

        db_user = User.query.filter_by(email=validated_data["email"]).first()
        
        if not db_user:
            raise ResponseError(code=400, description="Invalid credentials")
        
        if not check_password_hash(db_user.password, validated_data["password"]):
            raise ResponseError(code=400, description="Invalid credentials")
        
        access_token = create_access_token(
            identity=json.dumps({
                "id": db_user.id
            })
        )

        return {
            "status_code": 200,
            "message": "User login successfully",
            "data": {
                "access_token": access_token
            }
        }, 200


class LogoutResource(Resource):
    @jwt_required()
    def delete(self):
        jti = get_jwt()["jti"]
        
        blacklisted_token = TokenBlacklist(jti=jti)
        db.session.add(blacklisted_token)
        db.session.commit()

        return {
            "status_code": 200,
            "message": "User logout successfully"
        }, 200