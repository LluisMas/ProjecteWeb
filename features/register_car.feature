
Feature: Register Car
  # Enter feature description here

  Background: There is a registered user
    Given Exists a user "user" with password "password" and email "test@test.com" with Seller role
    Given Exists a user "customer" with password "password" and email "customer@customer.com" with Customer role
    And Exists a carshop with name "shopName" and email "test@test.com"


  Scenario: Register just Car
    Given I login as user "test@test.com" with password "password" and I am user "user"
    When I register a car at carshop "shopName"
      | name       |
      | Fish and Chips |
    Then I'm viewing the details page for car at carshop "shopName" by "test@test.com"
      | name       |
      | Fish and Chips |
    And There are 1 cars

  Scenario: Register a Car with Customer role
    Given I login as user "customer@customer.com" with password "password" and I am user "customer"
    When I register a car at carshop "shopName"
      | name       |
      | Fish and Chips |
    And There are 0 cars


  Scenario: Register a Car two times
    Given I login as user "test@test.com" with password "password" and I am user "user"
    When I register a car at carshop "shopName"
      | name       |
      | Fish and Chips |
    When I register a car at carshop "shopName"
      | name       |
      | Fish and Chips |
    And There are 1 cars

