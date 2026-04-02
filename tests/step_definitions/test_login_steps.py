from pytest_bdd import given, when, then, scenarios

@when("I send login request with valid credentials")
def login(reqres_client, context):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = reqres_client.post("/register", data=payload)

    context["response"] = response