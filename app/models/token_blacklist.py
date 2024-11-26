from app.extentions import db
import uuid

class TokenBlacklist(db.Model):
    __tablename__ = 'token_blacklists'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    jti = db.Column(db.String(255), unique=True, nullable=False)  # the unique id of jwt token
    revoked = db.Column(db.Boolean, default=False)

    def __init__(self, jti):
        self.jti = jti