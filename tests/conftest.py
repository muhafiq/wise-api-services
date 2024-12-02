import pytest
from app.app import app
from app.app import db
from app.models.users import User
from werkzeug.security import generate_password_hash
import re

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def cleanup_db():
    yield
    
    db.session.query(User).delete()  
    db.session.commit()

@pytest.fixture
def create_user(client):
    payload = {
        "name": "test",
        "email": "test@mail.com",
        "no_hp": "08312312332",
        "password": "password",
        "confirm_password": "password"
    }
    res = client.post("/api/v1/auth/register", json=payload)

    assert res.status_code == 201
    assert res.json.get("status_code") == 201
    assert res.json.get("message") == "User created."
    assert re.match(r"^[a-f0-9\-]{36}$", res.json.get("data")["id"])

    yield

@pytest.fixture
def login_user(client, create_user):
    user = {
        "email": "test@mail.com",
        "password": "password"
    }
    res = client.post("/api/v1/auth/login", json=user)

    assert res.status_code == 200

    yield res.json.get("data").get("access_token")