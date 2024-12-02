from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
import tensorflow as tf
import os
from google.cloud import storage

EXTENSIONS_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(EXTENSIONS_DIR, '..', 'model', 'model.h5')

# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(EXTENSIONS_DIR, '..', 'gcs-credentials.json')

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = JWTManager()
model = tf.keras.models.load_model(MODEL_PATH)

# google cloud storage client
storage_client = storage.Client()
bucket = storage_client.bucket(os.environ.get('GCS_BUCKET_NAME', ''))