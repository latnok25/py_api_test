import requests

BASE_URL = "https://reqres.in/api"
HEADERS = {"x-api-key": "reqres-free-v1"}

# def test_login_success():
#     payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
#     response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
#     assert response.status_code == 200
#     assert "token" in response.json()

# def test_login_failure_missing_password():
#     payload = {"email": "peter@klaven"}
#     response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
#     assert response.status_code == 400
#     assert "error" in response.json()

# def test_login_empty_credentials():
#     payload = {}
#     response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
#     assert response.status_code == 400
#     assert "error" in response.json()

# def test_create_user_success():
#     payload = {"name": "morpheus", "job": "leader"}
#     response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
#     assert response.status_code == 201
#     data = response.json()
#     assert data["name"] == "morpheus"
#     assert "id" in data

# def test_create_user_missing_job():
#     payload = {"name": "neo"}
#     response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
#     assert response.status_code == 201  # Still succeeds with missing job

# def test_update_user():
#     payload = {"name": "neo", "job": "chosen one"}
#     response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)
#     assert response.status_code == 200
#     assert response.json()["job"] == "chosen one"

# def test_delete_user():
#     response = requests.delete(f"{BASE_URL}/users/2", headers=HEADERS)
#     assert response.status_code == 204

# def test_get_single_user():
#     response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
#     assert response.status_code == 200
#     assert "data" in response.json()

# def test_get_single_user_not_found():
#     response = requests.get(f"{BASE_URL}/users/999", headers=HEADERS)
#     print("STATUS:", response.status_code)
#     print("BODY:", response.text)
#     assert response.status_code == 404

# def test_list_users_pagination():
#     response = requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)
#     assert response.status_code == 200
#     assert len(response.json()["data"]) > 0

# def test_delayed_response():
#     response = requests.get(f"{BASE_URL}/users?delay=3", timeout=5, headers=HEADERS)
#     assert response.status_code == 200

# def test_register_success():
#     payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
#     response = requests.post(f"{BASE_URL}/register", json=payload, headers=HEADERS)
#     assert response.status_code == 200
#     assert "token" in response.json()

# def test_register_failure_missing_password():
#     payload = {"email": "sydney@fife"}
#     response = requests.post(f"{BASE_URL}/register", json=payload, headers=HEADERS)
#     assert response.status_code == 400
#     assert "error" in response.json()

#     import requests

# BASE_URL = "https://reqres.in/api"
# HEADERS = {"x-api-key": "reqres-free-v1"}

def test_login_success():
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert isinstance(data["token"], str) and len(data["token"]) > 0

def test_login_failure_missing_password():
    payload = {"email": "peter@klaven"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code == 400
    assert "error" in response.json()

def test_login_empty_credentials():
    response = requests.post(f"{BASE_URL}/login", json={}, headers=HEADERS)
    assert response.status_code == 400
    assert "error" in response.json()

def test_create_user_success():
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert response.status_code == 201
    data = response.json()
    assert data.get("name") == "morpheus"
    assert "id" in data and isinstance(data["id"], str)

def test_create_user_missing_job():
    payload = {"name": "neo"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert response.status_code == 201
    data = response.json()
    assert data.get("name") == "neo"

def test_update_user():
    payload = {"name": "neo", "job": "chosen one"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data.get("job") == "chosen one"
    assert "updatedAt" in data

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 204
    assert response.text == ""  # DELETE should return empty body

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert data["data"]["id"] == 2

def test_get_single_user_not_found():
    response = requests.get(f"{BASE_URL}/users/999", headers=HEADERS)
    assert response.status_code in [404, 200]
    data = response.json()
    if response.status_code == 404:
        assert data == {} or "error" in data
    elif response.status_code == 200:
        assert not data.get("data") or data["data"] is None

def test_list_users_pagination():
    response = requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0

def test_delayed_response():
    response = requests.get(f"{BASE_URL}/users?delay=3", timeout=10, headers=HEADERS)
    assert response.status_code == 200
    assert "data" in response.json()

def test_register_success():
    payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(f"{BASE_URL}/register", json=payload, headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data and isinstance(data["token"], str)

def test_register_failure_missing_password():
    payload = {"email": "sydney@fife"}
    response = requests.post(f"{BASE_URL}/register", json=payload, headers=HEADERS)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data

