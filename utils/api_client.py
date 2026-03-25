import time
import requests
from config.config import BASE_URL, TIMEOUT
from utils.logger import get_logger

logger = get_logger(__name__)


def send_request(method, endpoint, payload=None, headers=None, timeout=TIMEOUT):
    url = f"{BASE_URL}{endpoint}"
    retries = 3

    for attempt in range(1, retries + 1):
        try:
            logger.info(f"Attempt {attempt} - {method} Request URL: {url}")

            if payload:
                logger.info(f"Request Payload: {payload}")

            response = requests.request(
                method=method,
                url=url,
                json=payload,
                headers=headers,
                timeout=timeout
            )

            logger.info(f"Response Status: {response.status_code}")
            logger.info(f"Response Body: {response.text}")

            # Retry only for server errors
            if response.status_code >= 500:
                logger.warning("Server error detected, retrying...")
                raise Exception("Server error")

            return response

        except requests.exceptions.Timeout:
            logger.error(f"{method} request timed out")

        except requests.exceptions.RequestException as e:
            logger.error(f"{method} request failed: {e}")

        if attempt < retries:
            logger.info(f"Retrying {method} request...")
            time.sleep(2)
        else:
            logger.error(f"Max retries reached for {method}")
            raise

def get(endpoint, headers=None):
    return send_request("GET", endpoint, headers=headers)


def post(endpoint, payload, headers=None):
    return send_request("POST", endpoint, payload=payload, headers=headers)


def put(endpoint, payload, headers=None):
    return send_request("PUT", endpoint, payload=payload, headers=headers)


def delete(endpoint, headers=None):
    return send_request("DELETE", endpoint, headers=headers)