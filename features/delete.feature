Feature: Trying to delete all the deletable things with any role.

  Background: There are an instance of every deletable objects
    Given Exists a user "seller" with password "seller" and email "seller@seller.com" with Seller role
    Given Exists a user "customer" with password "customer" and email "customer@customer.com" with Customer role
    And Exists a carshop with name "shopName" and email "seller@seller.com"


    Scenario: Delete a car with Seller role
      Given I login as user "seller@seller.com" with password "seller" and I am user "seller"
      When I register a car at carshop "shopName"
      | name       |
      | Fish and Chips |
      Then I'm viewing the details page for car at carshop "shopName" by "seller@seller.com"
      | name       |
      | Fish and Chips |
      And There is "Eliminar" link available