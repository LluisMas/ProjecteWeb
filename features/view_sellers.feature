Feature: View Seller
  In order to know about a seller
  As a user with Seller romle
I want to view the registered seller details

  Background: There is a registered user and car
      Given Exists a user "user" with password "password" and email "test@test.com" with Seller role
      Given Exists a user "customer" with password "password" and email "customer@customer.com" with Customer role

  Scenario: View details about a Seller not logged in
     Given I'm not logged in
     When I view the list of Sellers
     Then The list of Sellers is not displayed

   Scenario: View details about a Seller logged as customer
     Given I login as user "customer@customer.com" with password "password" and I am user "customer"
     When I view the list of Sellers
     Then The list of Sellers is not displayed


   Scenario: View details about a Seller logged as Seller
     Given I login as user "test@test.com" with password "password" and I am user "user"
     When I view the list of Sellers
     Then The list of Sellers is displayed
     And Seller list contains 1 seller