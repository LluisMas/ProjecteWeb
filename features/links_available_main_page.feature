Feature: Check if the links are available in the main page

  Background: There is a Customer and a Seller
    Given Exists a user "customer" with password "customer" and email "customer@customer" with Customer role
    And Exists a user "seller" with password "seller" and email "seller@seller.com" with Seller role

  Scenario: Check if there is links available being Customer
    Given I visit the main page
    And I login as user "customer@customer" with password "customer" and I am user "customer"
    Then There is "Concesionarios" text available
    And There is "Car" text available
    And There is no "Seller" text available
    And There is no "Sell" text available
    And There is no "Customer" text available


  Scenario: Check if there is links available without being logged
    Given I visit the main page
    And I'm not logged in
    Then There is "Concesionarios" text available
    And There is "Car" text available
    And There is no "Seller" text available
    And There is no "Sell" text available
    And There is no "Customer" text available

  Scenario: Check if there is links available being Seller
    Given I visit the main page
    And I login as user "customer@customer" with password "customer" and I am user "customer"
    Then There is "Concesionarios" text available
    And There is "Car" text available
    And There is "Seller" text available
    And There is "Sell" text available
    And There is "Customer" text available


