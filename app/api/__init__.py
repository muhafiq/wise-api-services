from flask import Blueprint
from flask_restful import Api
from app.extentions import jwt
from app.models.token_blacklist import TokenBlacklist

"""Resources"""
from .resources.auth import RegisterResource, LoginResource, LogoutResource
from .resources.user import UserResource

router = Blueprint("router", __name__, url_prefix="/api/v1")
api = Api(router, errors=router.errorhandler)

api.add_resource(RegisterResource, "/auth/register", endpoint="register")
api.add_resource(LoginResource, "/auth/login", endpoint="login")
api.add_resource(LogoutResource, "/auth/logout", endpoint="logout")
api.add_resource(UserResource, "/users/me", endpoint="users")


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return TokenBlacklist.query.filter_by(jti=jti, revoked=False).first() is not None
