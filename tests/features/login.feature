Feature: Login API

  Scenario: Successful login
    Given the API is available
    When I send login request with valid credentials
    Then the response status should be 200
    And I should receive a token