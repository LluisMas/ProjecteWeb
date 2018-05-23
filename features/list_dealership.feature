Feature: List Distributors
  I want to see the distributors' list


  Background: There are 6 registered Distributors
    Given Exists a user "test" with password "test" and email "test@test.com" with Seller role
    And Exists dealerships registered by "test@test.com"
    | shopName  | address |
    | One       | street1 |
    | Two       | street2 |
    | Three     | street3 |
    | Four      | street4 |
    | Five      | street5 |
    | Six       | street6 |


  Scenario: List all the Dealerships
    When I list dealerships
    Then I'm viewing a list containing
      | shopName  |
      | One       |
      | Two       |
      | Three     |
      | Four      |
      | Five      |
      | Six       |
    And list contains 6 Dealerships






