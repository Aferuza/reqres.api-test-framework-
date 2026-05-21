
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