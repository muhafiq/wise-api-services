from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from .error import ResponseError

"""Resources"""
from .resources.auth import RegisterResource, LoginResource, LogoutResource

router = Blueprint("router", __name__, url_prefix="/api/v1")
api = Api(router, errors=router.errorhandler)

api.add_resource(RegisterResource, "/auth/register", endpoint="register")
api.add_resource(LoginResource, "/auth/login", endpoint="login")
api.add_resource(LogoutResource, "/auth/logout", endpoint="logout")

@router.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return {
        "status_code": 400,
        "errors": e.messages
    }, 400

@router.errorhandler(ResponseError)
def handle_response_error(e):
    return {
        "status_code": e.code,
        "message": e.description,
        "error": True
    }, e.code

@router.app_errorhandler(404)
def handle_not_found_error(e):
    return {
        "status_code": 404,
        "message": "Resource not found"
    }, 404

@router.app_errorhandler(405)
def handle_method_not_allowed(e):
    return {
        "status_code": 404,
        "message": "Resource not found"
    }, 404

@router.app_errorhandler(500)
def handle_server_error(e):
    return {
        "status_code": 500,
        "message": "Something went wrong"
    }, 500