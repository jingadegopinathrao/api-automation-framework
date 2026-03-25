import pytest
from utils.data_reader import read_json
from config.config import BASE_URL
import requests

# Load test data from JSON file
test_data = read_json("data/post_test_data.json")


@pytest.mark.regression
@pytest.mark.parametrize("payload", test_data)
def test_create_post(payload):
    """
    Test to create posts using multiple datasets (Data-Driven Testing)
    """

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    # Validate status code
    assert response.status_code == 201

    # Validate response body
    response_json = response.json()

    assert response_json["title"] == payload["title"]
    assert response_json["body"] == payload["body"]
    assert response_json["userId"] == payload["userId"]