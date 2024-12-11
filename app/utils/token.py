import random
import time

def generate_token():
    token = f"{random.randint(100000, 999999)}"

    # menghitung waktu kedaluwarsa dalam 1 jam dari waktu sekarang
    expiration_time = int(time.time()) + 3600  # 3600 detik = 1 jam

    return f"{token}-{expiration_time}"

def validate_token(token):
    try:
        token_value, expiration_timestamp = token.split('-')

        if int(time.time()) > int(expiration_timestamp):
            return False  # Token sudah kedaluwarsa
        return True  # Token masih valid
    except AttributeError as e:
        return "You don't have a valid token, please request again!"
