import re

"""REGISTER TESTING"""

REG_ENDPOINT = "/api/v1/auth/register"

def test_register_success(client):
    payload = {
        "name": "test",
        "email": "test@mail.com",
        "no_hp": "08312312332",
        "password": "password",
        "confirm_password": "password"
    }
    res = client.post(REG_ENDPOINT, json=payload)

    assert res.status_code == 201
    assert res.json.get("status_code") == 201
    assert res.json.get("message") == "User created."
    assert re.match(r"^[a-f0-9\-]{36}$", res.json.get("data")["id"])

def test_register_error_no_payload(client):
    payload = {}
    res = client.post(REG_ENDPOINT, json=payload)

    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "Payload cannot be empty!"
    assert res.json.get("error") == True


def test_register_error_different_confirm_password(client):
    payload = {
        "name": "test",
        "email": "test@mail.com",
        "no_hp": "08312312332",
        "password": "password",
        "confirm_password": "password_wrong"
    }
    res = client.post(REG_ENDPOINT, json=payload)

    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "Validation error!"
    assert res.json.get("errors")["confirm_password"][0] == "Password and confirm password must match."

def test_register_error_payload_not_complete(client):
    payload = { # no no_hp payload
        "name": "test",
        "email": "test@mail.com",
        "password": "password",
        "confirm_password": "password"
    }
    res = client.post(REG_ENDPOINT, json=payload)

    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "Validation error!"
    assert res.json.get("errors")["no_hp"][0] == "This field is required."
    """this test also work in all required field"""

def test_register_error_unknown_field(client):
    payload = {
        "name": "test",
        "email": "test@mail.com",
        "no_hp": "08312312332",
        "password": "password",
        "confirm_password": "password",
        "data": "i wanna hack you" # the unknown field
    }
    res = client.post(REG_ENDPOINT, json=payload)

    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "Validation error!"
    assert res.json.get("errors")["data"][0] == "Unknown field."
    """this test also work in all unknown field"""

def test_register_error_duplicate_email(client):
    payload = {
        "name": "test",
        "email": "test@mail.com",
        "no_hp": "08312312332",
        "password": "password",
        "confirm_password": "password"
    }
    res = client.post(REG_ENDPOINT, json=payload)

    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "Validation error!"
    assert res.json.get("errors")["email"][0] == "Email already exist."

def test_register_error_format_not_json(client):
    payload = "sebuah payload"
    res = client.post(REG_ENDPOINT, json=payload)

    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "Validation error!"
    assert res.json.get("errors")["_schema"][0] == "Invalid input type."

"""END OF REGISTER TESTING"""


"""LOGIN TESTING"""

LOGIN_ENDPOINT = "/api/v1/auth/login"

def test_login_success(client):
    payload = {
        "email": "test@mail.com",
        "password": "password"
    }
    res = client.post(LOGIN_ENDPOINT, json=payload)
    assert res.status_code == 200
    assert res.json.get("status_code") == 200
    assert res.json.get("message") == "User login successfully"
    assert "access_token" in res.json.get("data")

    global access_token
    access_token = res.json.get("data").get("access_token")
    
def test_login_email_not_found(client):
    payload = {
        "email": "notfound@mail.com",
        "password": "password"
    }
    res = client.post(LOGIN_ENDPOINT, json=payload)
    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "Invalid credentials"

def test_login_invalid_email(client):
    payload = {
        "email": "test@mail",
        "password": "password"
    }
    res = client.post(LOGIN_ENDPOINT, json=payload)
    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "Validation error!"
    assert "email" in res.json.get("errors")

def test_login_invalid_password(client):
    payload = {
        "email": "test@mail.com",
        "password": "wrongpassword"
    }
    res = client.post(LOGIN_ENDPOINT, json=payload)
    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "Invalid credentials"

def test_login_empty_payload(client):
    res = client.post(LOGIN_ENDPOINT, json={})
    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "Payload cannot be empty!"

def test_login_missing_password(client):
    payload = {
        "email": "test@mail.com"
    }
    res = client.post(LOGIN_ENDPOINT, json=payload)
    assert res.status_code == 400
    assert "password" in res.json.get("errors")

"""END OF LOGIN TESTING"""

"""LOGOUT TESTING"""

LOGOUT_ENDPOINT = "/api/v1/auth/logout"

def test_logout_success(client):
    global access_token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    res = client.delete(LOGOUT_ENDPOINT, headers=headers)
    assert res.status_code == 200
    assert res.json.get("message") == "User logout successfully"

def test_missing_authorization_header(client):
    res = client.delete(LOGOUT_ENDPOINT)
    assert res.status_code == 401
    assert res.json.get("message") == "No token provided!"
    assert res.json.get("error") == "Unauthorized"

def test_invalid_token(client):
    headers = {
        "Authorization": "Bearer invalidtoken"
    }
    res = client.delete(LOGOUT_ENDPOINT, headers=headers)
    assert res.status_code == 422
    assert "msg" in res.json

def test_expired_token(client):
    global access_token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    res = client.delete(LOGOUT_ENDPOINT, headers=headers)
    assert res.status_code == 401
    assert res.json.get("message") == "Token is expired or revoked!"
    assert res.json.get("error") == "Unauthorized"

def test_blacklisted_token(client, cleanup_db):
    global access_token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    res = client.delete(LOGOUT_ENDPOINT, headers=headers)
    assert res.status_code == 401
    assert res.json.get("message") == "Token is expired or revoked!"
    assert res.json.get("error") == "Unauthorized"


"""END OF LOGOUT TESTING"""