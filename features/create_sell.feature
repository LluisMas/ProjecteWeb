# Created by lmr at 17/05/18
Feature: Register Sell

 Background: There is a registered user and car
    Given Exists a user "user" with password "password" and email "test@test.com" with Seller role
    Given Exists a user "customer" with password "password" and email "customer@customer.com" with Customer role
    And Exists a car with name "troncomovil"

  Scenario: Register a Sell
    Given I login as user "test@test.com" with password "password" and I am user "user"
    When I register sell for car "troncomovil"
      | Date |
      | 2018-05-17 |
    Then I'm viewing the details of the sell "troncomovil"
      | Date       |
      | 2018-05-17 |
    And There are 1 sell
    And Car "troncomovil" is set as sold

  Scenario: Register a Sell being a customer
    Given I login as user "customer@customer.com" with password "password" and I am user "customer"
    When I register sell for car "troncomovil"
      | Date |
      | 2018-05-17 |
    And There are 0 sell


