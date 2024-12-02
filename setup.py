"""
File ini digunakan untuk download file model dari cloud
ke local, karena model .h5 tidak bisa di load lewat url
dan ukuran file .h5 terlalu besar untuk masuk ke github repository
"""

import os
import urllib.request
from dotenv import load_dotenv

load_dotenv()

MODEL_URL = os.environ.get("MODEL_URL", "")

MODEL_DIR = "./model"
MODEL_PATH = os.path.join(MODEL_DIR, "model.h5")

os.makedirs(MODEL_DIR, exist_ok=True)

print(f"Downloading model from {MODEL_URL}...")
urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")
