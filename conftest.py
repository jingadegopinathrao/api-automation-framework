import pytest
from utils.api_client import APIClient


@pytest.fixture(scope="session")
def json_client():
    return APIClient(api_type="json")


@pytest.fixture(scope="session")
def reqres_client():
    return APIClient(api_type="reqres")