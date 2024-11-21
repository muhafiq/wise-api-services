from app.extentions import db
from sqlalchemy.sql import func
import uuid

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(120), unique=True, nullable=False)
    no_hp = db.Column(db.String(16), nullable=False)
    password = db.Column(db.Text, nullable=False)
    refresh_token = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=func.now(), nullable=True)