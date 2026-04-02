import requests
import allure
from utils.config import JSON_BASE_URL, REQRES_BASE_URL, TIMEOUT
from utils.logger import logger


class APIClient:
    def __init__(self, api_type="json"):
        if api_type == "json":
            self.base_url = JSON_BASE_URL
        elif api_type == "reqres":
            self.base_url = REQRES_BASE_URL
        else:
            raise ValueError("Invalid API type")

        self.headers = {
            "Accept": "application/json",
            "User-Agent": "pytest-framework"
        }

    def attach(self, name, data):
        allure.attach(
            str(data),
            name=name,
            attachment_type=allure.attachment_type.JSON
        )

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"GET → {url}")
        self.attach("Request URL", url)

        response = requests.get(url, headers=self.headers, timeout=TIMEOUT)

        logger.info(f"Status → {response.status_code}")
        logger.debug(response.text)

        self.attach("Response Status", response.status_code)
        self.attach("Response Body", response.text)

        return response

    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"POST → {url}")
        logger.debug(f"Payload → {data}")

        self.attach("Request URL", url)
        self.attach("Request Payload", data)

        response = requests.post(url, json=data, headers=self.headers, timeout=TIMEOUT)

        logger.info(f"Status → {response.status_code}")
        logger.debug(response.text)

        self.attach("Response Status", response.status_code)
        self.attach("Response Body", response.text)

        return response

    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"PUT → {url}")
        self.attach("Request URL", url)
        self.attach("Request Payload", data)

        response = requests.put(url, json=data, headers=self.headers, timeout=TIMEOUT)

        self.attach("Response Status", response.status_code)
        self.attach("Response Body", response.text)

        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"DELETE → {url}")
        self.attach("Request URL", url)

        response = requests.delete(url, headers=self.headers, timeout=TIMEOUT)

        self.attach("Response Status", response.status_code)
        self.attach("Response Body", response.text)

        return response