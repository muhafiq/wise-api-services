from app.extentions import bucket
from werkzeug.utils import secure_filename
import os
from datetime import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Fungsi untuk memeriksa ekstensi file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def normalize_file_name(filename):
    filename = secure_filename(filename)

    base, ext = os.path.splitext(filename)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    normalized_filename = f"{base}_{timestamp}{ext}"

    return normalized_filename

def upload_image(file):
    file.seek(0)

    filename = normalize_file_name(file.filename)
    blob_name = f'app/{filename}'

    # Upload file ke bucket Google Cloud Storage
    blob = bucket.blob(blob_name)
    blob.upload_from_file(file)

    # Dapatkan URL file yang diupload
    file_url = blob.public_url

    return file_url