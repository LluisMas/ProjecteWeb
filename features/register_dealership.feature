Feature: Register Dealership
  # Enter feature description here
  #
  #
  Background: There is a registered user and restaurant
    Given Exists a user "user" with password "password" and email "test@test.com" with Seller role
    Given Exists a user "customer" with password "password" and email "customer@customer.com" with Customer role


  Scenario: Register a Dealership
    Given I login as user "test@test.com" with password "password" and I am user "user"
    When I register dealership
      | shopName       |
      | Fish and Chips |
    Then I'm viewing the details page for dealership by "test@test.com"
      | shopName       |
      | Fish and Chips |
    And There are 1 dealerships

  Scenario: Register a Dealership with Customer role
    Given I login as user "customer@customer.com" with password "password" and I am user "customer"
    When I register dealership
      | shopName       |
      | Fish and Chips |
    And There are 0 dealerships


  Scenario: Register a Dealership two times
    Given I login as user "test@test.com" with password "password" and I am user "user"
    When I register dealership
      | shopName       |
      | Fish and Chips |
    When I register dealership
      | shopName       |
      | Fish and Chips |
    And There are 1 dealerships
