import pytest
import requests
from config.config import BASE_URL

@pytest.fixture
def auth_token():

    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "username": "testuser",
            "password": "test123"
        }
    )

    return response.json().get("token")