
import pytest
import requests
from config import BASE_URL, TIMEOUT, REQRES_API_TOKEN

@pytest.fixture(scope="session")
def api_client():
    """Provides an isolated HTTP client instance utilizing a pooled session."""
    session = requests.Session()
    # Intercept session requests to pre-populate base routing structures
    session.headers.update({
    "Content-Type": "application/json",
    "x-api-key": REQRES_API_TOKEN
    })
    yield session
    session.close()

@pytest.mark.parametrize("user_id,expected_status", [
    (1,    200),   # valid user
    (2,    200),   # valid user
    (9999, 404),   # non-existent
    (0,    404),   # boundary
])


def test_user_id_status_codes(api_client, user_id, expected_status):
    """Parametrized: validates multiple user IDs in one test function"""
    response = api_client.get(
        f"{BASE_URL}/users/{user_id}",
        timeout=TIMEOUT
    )
    assert response.status_code == expected_status, \
        f"User ID {user_id}: expected {expected_status}, got {response.status_code}"
