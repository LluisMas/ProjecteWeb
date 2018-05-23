Feature: View Customer
  In order to know about a customer
  As a user with Seller romle
I want to view the registered cutomer details

   Background: There is a registered user and car
      Given Exists a user "user" with password "password" and email "test@test.com" with Seller role
      Given Exists a user "customer" with password "password" and email "customer@customer.com" with Customer role



   Scenario: View details about a Customer
     Given I login as user "customer@customer.com" with password "password" and I am user "customer"
     When I view the list of Customers
     Then The list is not displayed


   Scenario: View details about a Customer being a Seller
     Given I login as user "test@test.com" with password "password" and I am user "user"
     When I view the list of Customers
     Then The list is displayed
     And Customer list contains 1 customers