from flask import Flask
from app.extentions import db, migrate, jwt
from app.config import config
from os import environ
from app.api import router
from app.api.error_handler import register_error_handler
from app.models.medical_records import MedicalRecord
from app.models.injury_classes import InjuryClass

app = Flask(__name__)
app.config.from_object(config[environ.get("APP_ENV", "default")])

app.register_blueprint(blueprint=router)

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

register_error_handler(app)