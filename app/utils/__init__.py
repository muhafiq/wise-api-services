from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np

def preprocess_image(file, target_size=(64, 64)):
    """
    Preprocessing gambar untuk digunakan sebagai input model.
    - Resize gambar ke ukuran target.
    - Normalisasi nilai piksel (0-255 menjadi 0-1).
    - Tambahkan dimensi batch.

    Args:
        file (file-like object): File gambar dari request.
        target_size (tuple): Ukuran target (height, width).

    Returns:
        numpy.ndarray: Array gambar yang sudah diproses.
    """
    img = Image.open(file)  # Buka file gambar
    img = img.resize(target_size)  # Resize gambar
    img_array = img_to_array(img)  # Konversi ke array NumPy
    img_array = img_array / 255.0  # Normalisasi (0-1)
    img_array = np.expand_dims(img_array, axis=0)  # Tambahkan dimensi batch

    return img_array

def after_prediction(prediction):
    class_names = [
        'Abrasions',
        'Bruises',
        'Burns',
        'Cut',
        'Ingrown_nails',
        'Laceration',
        'Stab_wound'
    ]

    predicted_class_idx = np.argmax(prediction, axis=1)[0]
    predicted_class_name = class_names[predicted_class_idx]

    return predicted_class_name