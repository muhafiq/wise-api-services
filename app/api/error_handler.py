from marshmallow import ValidationError
from .error import ResponseError
from flask_jwt_extended.exceptions import NoAuthorizationError, RevokedTokenError

def register_error_handler(app):

    @app.errorhandler(ValidationError)
    def handle_marshmallow_error(e):
        return {
            "status_code": 400,
            "message": "Validation error!",
            "errors": e.messages
        }, 400

    @app.errorhandler(ResponseError)
    def handle_response_error(e):
        return {
            "status_code": e.code,
            "message": e.description,
            "error": True
        }, e.code

    @app.errorhandler(NoAuthorizationError)
    def handle_unauthorized_error(e):
        return {
            "status_code": 401,
            "message": "No token provided!",
            "error": "Unauthorized"
        }, 401

    @app.errorhandler(RevokedTokenError)
    def handle_unauthorized_error(e):
        return {
            "status_code": 401,
            "message": "Token is expired or revoked!",
            "error": "Unauthorized"
        }, 401

    @app.errorhandler(404)
    def handle_not_found_error(e):
        return {
            "status_code": 404,
            "message": "Resource not found"
        }, 404

    @app.errorhandler(405)
    def handle_method_not_allowed(e):
        return {
            "status_code": 404,
            "message": "Resource not found"
        }, 404

    @app.errorhandler(500)
    def handle_server_error(e):
        return {
            "status_code": 500,
            "message": "Something went wrong"
        }, 500