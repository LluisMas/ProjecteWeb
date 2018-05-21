Feature: Register Dealership
  # Enter feature description here
  #
  #
  Background: There is a registered user and restaurant
    Given Exists a user "user" with password "password" and email "test@test.com"

  Scenario: Register a Dealership
    Given I login as user "test@test.com" with password "password" and I am user "user"
    When I register dealership
      | shopName       |
      | Fish and Chips |
    Then I'm viewing the details page for dealership by "test@test.com"
      | shopName       |
      | Fish and Chips |
    And There are 1 dealerships