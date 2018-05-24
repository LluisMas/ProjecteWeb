# Created by lmr at 24/05/18
Feature: Register Review
  In order to share my opinion about a dealership
  As a user
  I want to register a review with rating and comment about a dealership

  Background: There is a user and a dealership
    Given Exists a user "seller" with password "seller" and email "seller@seller.com" with Seller role
    And Exists a user "customer" with password "customer" and email "customer@customer.com" with Customer role
    And Exists dealership registered by the user "seller@seller.com" with name "PawnShop"

  Scenario: Register review with rating and comment
    Given I login as user "customer@customer.com" with password "customer" and I am user "customer"
    When I register a review at carshop "PawnShop"
    | rating          | comment                          |
    | 4               | Best stolen cars in the city     |
    Then I'm viewing the details page for dealership with name "PawnShop"