import allure


@allure.feature("Users API")
@allure.story("Get Users")
@allure.title("Verify GET Users API with valid response")
@allure.description("This test verifies users API response")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("API", "Regression")
def test_get_users(json_client):

    with allure.step("Send GET request"):
        response = json_client.get("/users")

    with allure.step("Validate status code"):
        assert response.status_code == 200

    with allure.step("Validate response is not empty"):
        assert len(response.json()) > 0