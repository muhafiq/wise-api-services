import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30) # 30 days token expired

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False

config = {
    "development": DevConfig,
    "production": ProdConfig,
    "default": DevConfig
}
