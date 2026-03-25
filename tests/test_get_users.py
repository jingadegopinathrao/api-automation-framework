import pytest
from utils.api_client import get


@pytest.mark.smoke
def test_get_users():
    """
    Test to fetch users
    """

    response = get("/users")

    assert response.status_code == 200

    response_json = response.json()

    assert isinstance(response_json, list)
    assert len(response_json) > 0

    first_user = response_json[0]

    assert "id" in first_user
    assert "name" in first_user
    assert "email" in first_user