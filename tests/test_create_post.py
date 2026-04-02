import pytest
from utils.data_reader import read_json

test_data = read_json("data/post_test_data.json")


@pytest.mark.regression
@pytest.mark.parametrize("payload", test_data)
def test_create_post(json_client, payload):   # ✅ use fixture
    response = json_client.post("/posts", data=payload)

    assert response.status_code == 201

    response_json = response.json()

    assert response_json["title"] == payload["title"]
    assert response_json["body"] == payload["body"]
    assert response_json["userId"] == payload["userId"]