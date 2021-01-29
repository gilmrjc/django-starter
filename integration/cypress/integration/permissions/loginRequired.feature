Feature: Login required

  All pages should required to be logged in

  Scenario: Homepage
    When I open the homepage
    Then I am redirected to the login page

  Scenario: Vacancies
    When I open the vacancies list
    Then I am redirected to the login page

  Scenario: Candidates
    When I open the candidates list
    Then I am redirected to the login page

  Scenario: Clients
    When I open the clients list
    Then I am redirected to the login page

  Scenario: Recruiters
    When I open the recruiters list
    Then I am redirected to the login page
