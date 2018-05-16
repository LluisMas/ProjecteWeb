Feature: Register Dealership
  # Enter feature description here
  #
  #
  Background: There is a registered user and restaurant
    Given Exists a user "user" with password "password"

  Scenario: Register a Dealership
    Given I login as user "user" with password "password"
    When I register dealership
      | shopName       |
      | Fish and Chips |
    Then I'm viewing the details page for dealership by "user"
      | shopName       |
      | Fish and Chips |
    And There are 1 dealerships