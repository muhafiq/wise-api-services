from flask import Flask
from app.extentions import db, migrate, jwt
from app.config import config
from os import environ
from app.api import router

app = Flask(__name__)
app.config.from_object(config[environ.get("APP_ENV", "default")])

app.register_blueprint(blueprint=router)

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

