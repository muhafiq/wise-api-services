from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
import tensorflow as tf
import os

EXTENSIONS_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(EXTENSIONS_DIR, '..', 'model', 'model.h5')

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = JWTManager()
model = tf.keras.models.load_model(MODEL_PATH)