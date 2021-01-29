Feature: Account creation

  Scenario: New accounts require email verification
    When a visitor creates a new account with:
      | name | last name | password        |
      | Juan | Perez     | testingpassword |
    Then a verify email message is displayed
    And the user has 1 email with the confirmation code

  Scenario: New accounts need to login after email verification
    When a visitor creates a new account with:
      | name | last name | password        |
      | Juan | Perez     | testingpassword |
    And the user verifies its email
    Then the user is redirected to the login page

  Scenario: New users need to verify email to login
    When a visitor creates a new account with:
      | name | last name | password        |
      | Juan | Perez     | testingpassword |
    And the user logins
    Then a verify email message is displayed
    And the user has 2 emails with the confirmation code
