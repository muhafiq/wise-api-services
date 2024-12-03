from app.extentions import db
from sqlalchemy.sql import func
import uuid

class MedicalRecord(db.Model):
    __tablename__ = 'medical_records'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    photo_date = db.Column(db.DateTime, nullable=False, default=func.now())  # Tanggal foto
    diagnosis_id = db.Column(db.String(36), db.ForeignKey('injury_classes.id'), nullable=False)  # Kategori luka (foreign key)
    treatment = db.Column(db.Text, nullable=False)  # Penanganan luka
    photo = db.Column(db.String(255), nullable=False)  # Path atau URL foto luka (misalnya nama file atau URL)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=func.now(), nullable=True)
    # Relasi opsional ke User
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=True)
    
    # Relasi dengan tabel InjuryClass
    diagnosis = db.relationship('InjuryClass', backref=db.backref('medical_records', lazy=True))