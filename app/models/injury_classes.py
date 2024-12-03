from app.extentions import db
from sqlalchemy.sql import func
import uuid

class InjuryClass(db.Model):
    __tablename__ = 'injury_classes'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    class_name = db.Column(db.String(50), nullable=False, unique=True)
    treatment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=func.now(), nullable=True)