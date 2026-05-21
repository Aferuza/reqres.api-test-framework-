
import pytest
from config import BASE_URL, TIMEOUT, REQRES_API_TOKEN

def test_list_users_pagination(api_client):
    """Test 1: Verify user listing pagination structure and status code."""
    response = api_client.get(f"{BASE_URL}/users", params={"page": 2}, timeout=TIMEOUT)

    assert response.status_code == 200
    json_data = response.json()
    assert json_data["page"] == 2
    assert "data" in json_data
    assert len(json_data["data"]) > 0


def test_single_user_found(api_client):
    """Test 2: Verify structural data integrity of a specific targeted user lookup."""
    response = api_client.get(f"{BASE_URL}/users/2", timeout=TIMEOUT)

    assert response.status_code == 200
    user_data = response.json()["data"]
    assert user_data["id"] == 2
    assert "email" in user_data
    assert user_data["first_name"] == "Janet"


def test_single_user_not_found(api_client):
    """Test 3: Negative test path evaluating the edge retrieval for an invalid ID."""
    response = api_client.get(f"{BASE_URL}/users/23", timeout=TIMEOUT)

    assert response.status_code == 404
    assert response.json() == {}  # Expecting clean structural empty return


def test_list_resource_colors(api_client):
    """Test 4: Validate underlying core asset lookup metrics and data schema."""
    response = api_client.get(f"{BASE_URL}/unknown", timeout=TIMEOUT)

    assert response.status_code == 200
    json_data = response.json()
    assert "total_pages" in json_data
    # Check schema definition of initial array item
    first_item = json_data["data"][0]
    assert "pantone_value" in first_item
    assert  "color" in first_item

def test_create_user_successful(api_client):
    """Test 5: Verify post mutations accurately persist user records."""
    payload = {"name": "morpheus", "job": "leader"}
    response = api_client.post(f"{BASE_URL}/users", json=payload, timeout=TIMEOUT)

    assert response.status_code == 201
    json_data = response.json()
    assert json_data["name"] == "morpheus"
    assert json_data["job"] == "leader"
    assert "id" in json_data
    assert "createdAt" in json_data

# PUT/PATCH ENGINES (UPDATE)

def test_update_user_via_put(api_client):
    """Test 6: Validate absolute structural payload updates via PUT strategy."""
    payload = {"name": "morpheus", "job": "zion resident"}
    response = api_client.put(f"{BASE_URL}/users/2", json=payload, timeout=TIMEOUT)

    assert response.status_code == 200
    assert response.json()["job"] == "zion resident"
    assert "updatedAt" in response.json()


def test_update_user_via_patch(api_client):
    """Test 7: Validate incremental mutation changes utilizing PATCH execution."""
    payload = {"job": "architect"}
    response = api_client.patch(f"{BASE_URL}/users/2", json=payload, timeout=TIMEOUT)

    assert response.status_code == 200
    assert response.json()["job"] == "architect"

# DELETE ENGINES (REMOVE)

def test_delete_user_successful(api_client):
    """Test 8: Ensure user removal operations match REST specification criteria."""
    response = api_client.delete(f"{BASE_URL}/users/2", timeout=TIMEOUT)

    # 204 No Content indicates server processed target deletion successfully
    assert response.status_code == 204
    assert response.text == ""


def test_register_user_successful(api_client):
    """Test 9: Verify user registration returns validation token parameters."""
    payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = api_client.post(f"{BASE_URL}/register", json=payload, timeout=TIMEOUT)

    assert response.status_code == 200
    json_data = response.json()
    assert "id" in json_data
    assert "token" in json_data


def test_login_user_missing_password(api_client):
    """Test 10: Fail-safes verification evaluating missing login credential inputs."""
    payload = {"email": "peter@klaven"}
    response = api_client.post(f"{BASE_URL}/login", json=payload, timeout=TIMEOUT)

    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"