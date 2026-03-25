from utils.api_client import post

payload = {
    "title": "API Testing",
    "body": "sample",
    "userId": 1
}

response = post("/posts", payload)