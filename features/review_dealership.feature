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
    And I'm viewing the reviews containing
    | rating          | comment                          |  user      |
    | 4               | Best stolen cars in the city     |  customer  |
    And list contains "1" review
    And There are "1" reviews


    Scenario: Try to register review but not logged
      Given I'm not logged in
      Then There is not "Add Review" link available
      And There are "0" reviews


    Scenario: Doing another review replaces the previous
      Given Exists review at dealership "PawnShop" by "customer"
      | rating          | comment                          |
      | 4               | Best stolen cars in the city     |
      And I login as user "customer@customer.com" with password "customer" and I am user "customer"
      When I register a review at carshop "PawnShop"
      | rating          | comment                          |
      | 1               | One worker harassed me           |
      Then I'm viewing the details page for dealership with name "PawnShop"
      And I'm viewing the reviews containing
      | rating          | comment                          |  user      |
      | 1               | One worker harassed me           |  customer  |

