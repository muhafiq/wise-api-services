from flask import Blueprint
from flask_restful import Api
from app.extentions import jwt
from app.models.token_blacklist import TokenBlacklist

"""Resources"""
from .resources.auth import RegisterResource, LoginResource, LogoutResource
from .resources.user import UserResource, ForgotPasswordResource, ResetPasswordResource, VerifyTokenResource
from .resources.predict import PredictResource
from .resources.history import AllHistoryResource, SingleHistoryResource, CancelAddHistoryRecord
from .resources.hospital import HospitalResource

router = Blueprint("router", __name__, url_prefix="/api/v1")
api = Api(router, errors=router.errorhandler)

api.add_resource(RegisterResource, "/auth/register", endpoint="register")
api.add_resource(LoginResource, "/auth/login", endpoint="login")
api.add_resource(LogoutResource, "/auth/logout", endpoint="logout")
api.add_resource(UserResource, "/users/me", endpoint="users")
api.add_resource(ForgotPasswordResource, "/users/forgot-password", endpoint="forgot_password")
api.add_resource(ResetPasswordResource, "/users/reset-password", endpoint="reset_password")
api.add_resource(VerifyTokenResource, "/users/verify-token", endpoint="verify_token")
api.add_resource(PredictResource, "/predict", endpoint="predict")
api.add_resource(AllHistoryResource, "/history", endpoint="history")
api.add_resource(SingleHistoryResource, "/history/<string:history_id>", endpoint="single_history")
api.add_resource(CancelAddHistoryRecord, "/history/cancel", endpoint="cancel_history")
api.add_resource(HospitalResource, "/nearby-hospitals", endpoint="hospitals")

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return TokenBlacklist.query.filter_by(jti=jti, revoked=False).first() is not None
