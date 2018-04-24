Feature: Register Persona

Scenario: Register just dish name
    Given I login as user "user" with password "password"
    When I register dish at restaurant "The Tavern"
      | name            |
      | Fish and Chips  |
    Then I'm viewing the details page for dish at restaurant "The Tavern" by "user"
      | name            |
      | Fish and Chips  |

And There are 1 dishes