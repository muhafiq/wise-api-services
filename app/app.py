from flask import Flask
from app.extentions import db, migrate, jwt
from app.config import config
from os import environ
from app.api import router
from app.api.error_handler import register_error_handler
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'

app = Flask(__name__)
app.config.from_object(config[environ.get("APP_ENV", "default")])

CORS(app)

app.register_blueprint(blueprint=router)
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Wise API"
    }
)
app.register_blueprint(swaggerui_blueprint)

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

register_error_handler(app)