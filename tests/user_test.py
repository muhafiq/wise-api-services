
"""GET USER PROFILE TESTING"""

GET_USER_ENDPOINT = "/api/v1/users/me"

def test_get_user_profile_success(client, login_user, cleanup_db):
    headers = {
        "Authorization": f"Bearer {login_user}"
    }
    res = client.get(GET_USER_ENDPOINT, headers=headers)

    assert res.status_code == 200
    assert res.json.get("status_code") == 200
    assert res.json.get("message") == "Get user profile successfully"
    assert res.json.get("data").get("name") == "test"

def test_get_user_without_access_token(client):
    res = client.get(GET_USER_ENDPOINT)

    assert res.status_code == 401
    assert res.json.get("status_code") == 401
    assert res.json.get("message") == "No token provided!"
    assert res.json.get("error") == "Unauthorized"

def test_get_user_with_invalid_access_token(client):
    headers = {
        "Authorization": "Bearer invalid_token"
    }
    res = client.get(GET_USER_ENDPOINT, headers=headers)

    assert res.status_code == 422
    assert "msg" in res.json

def test_get_user_with_expired_access_token(client, login_user, cleanup_db):
    headers = {
        "Authorization": f"Bearer {login_user}"
    }

    res = client.delete("/api/v1/auth/logout", headers=headers)

    res = client.get(GET_USER_ENDPOINT, headers=headers)

    assert res.status_code == 401
    assert res.json.get("status_code") == 401
    assert res.json.get("message") == "Token is expired or revoked!"
    assert res.json.get("error") == "Unauthorized"


"""END OF GET USER PROFILE TESTING"""


"""UPDATE USER PROFILE TESTING"""

UPDATE_USER_ENDPOINT = "/api/v1/users/me"

def test_update_profile_empty_payload(client, login_user, cleanup_db):
    headers = {"Authorization": f"Bearer {login_user}"}
    res = client.put(UPDATE_USER_ENDPOINT, headers=headers, json={})

    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "Payload cannot be empty!"

def test_update_profile_invalid_field(client, login_user, cleanup_db):
    headers = {"Authorization": f"Bearer {login_user}"}
    payload = {"password": "new_password", "address": "Invalid Address"}
    res = client.put(UPDATE_USER_ENDPOINT, headers=headers, json=payload)

    assert res.status_code == 400
    assert res.json.get("status_code") == 400
    assert res.json.get("message") == "No valid fields to update"

def test_update_profile_invalid_token(client):
    headers = {"Authorization": "Bearer invalid.jwt.token"}
    payload = {"name": "New Name", "email": "new@mail.com"}
    res = client.put(UPDATE_USER_ENDPOINT, headers=headers, json=payload)

    assert res.status_code == 422
    assert "msg" in res.json

def test_update_profile_success(client, login_user, cleanup_db):
    headers = {"Authorization": f"Bearer {login_user}"}
    payload = {"name": "Updated Name", "email": "updated@mail.com"}
    res = client.put(UPDATE_USER_ENDPOINT, headers=headers, json=payload)

    assert res.status_code == 200
    assert res.json["message"] == "User profile updated successfully"
    assert res.json["data"]["name"] == "Updated Name"
    assert res.json["data"]["email"] == "updated@mail.com"

def test_update_profile_no_changes(client, login_user, cleanup_db):
    headers = {"Authorization": f"Bearer {login_user}"}
    payload = {"name": "test", "email": "test@mail.com"}  # Sama dengan data awal
    res = client.put(UPDATE_USER_ENDPOINT, headers=headers, json=payload)

    assert res.status_code == 200
    assert res.json["data"]["name"] == "test"
    assert res.json["data"]["email"] == "test@mail.com"

def test_update_profile_unauthorized(client):
    res = client.put(UPDATE_USER_ENDPOINT, json={"name": "New Name"})

    assert res.status_code == 401
    assert res.json.get("message") == "No token provided!"
    assert res.json.get("error") == "Unauthorized"

"""END OF UPDATE USER PROFILE TESTING"""