import allure
from utils.api_client import get


@allure.feature("Users API")
@allure.story("Get Users")
# ✅ Add decorators HERE (above function)
@allure.title("Verify GET Users API with valid response")
@allure.description("This test verifies users API response")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("API", "Regression")
def test_get_users():
    # ✅ Step 1
    with allure.step("Send GET request"):
        response = get("/users")

        # Attach response
        allure.attach(
            response.text,
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )

    # ✅ Step 2
    with allure.step("Validate status code"):
        assert response.status_code == 200

    # ✅ Step 3
    with allure.step("Validate response is not empty"):
        assert len(response.json()) > 0
