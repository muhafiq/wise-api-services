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

def delete_image_by_url(public_url):
    """
    Menghapus file dari GCS berdasarkan public URL.

    Parameters:
    - public_url (str): URL publik dari file di GCS.

    Returns:
    - str: Pesan konfirmasi atau error.
    """
    try:
        # Ekstrak blob_name dari public URL
        base_url = "https://storage.googleapis.com/"
        if not public_url.startswith(base_url):
            return "Invalid URL", False

        blob_name = public_url.replace(base_url, "").split("/", 1)[1]

        blob = bucket.blob(blob_name)
        blob.delete()

        return f"File {blob_name} deleted successfully", True
    except Exception as e:
        return f"Error while trying to delete file: {e}", False
