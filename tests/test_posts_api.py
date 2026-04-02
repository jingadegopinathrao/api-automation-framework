import pytest
from utils.data_reader import read_json

test_data = read_json("data/post_test_data.json")


@pytest.mark.smoke
def test_get_posts(json_client):   # ✅ use fixture
    response = json_client.get("/posts")

    assert response.status_code == 200

    response_json = response.json()

    assert isinstance(response_json, list)
    assert len(response_json) > 0

    first_post = response_json[0]

    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post
    assert "userId" in first_post


@pytest.mark.regression
@pytest.mark.parametrize("payload", test_data)
def test_create_post(json_client, payload):   # ✅ use fixture
    response = json_client.post("/posts", data=payload)

    assert response.status_code == 201

    response_json = response.json()

    assert response_json["title"] == payload["title"]
    assert response_json["body"] == payload["body"]
    assert response_json["userId"] == payload["userId"]