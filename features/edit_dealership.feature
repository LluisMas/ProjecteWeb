Feature: Edit DealerShip
  In order to keep updated the previous registers about dealerships
  As a user
  I want to edit a dealership register I created

  Background: There are registered users and a dealership by one of them
    Given Exists a user "user" with password "password" and email "test@test.com" with Seller role
    Given Exists a user "customer" with password "password" and email "customer@customer.com" with Customer role
    And Exists dealership registered by "user"
      | shopName        | city            | country         |
      | The Tavern      | Los Angeles     | USA             |

  Scenario: Edit owned dealership registry country
    Given I login as user "test@test.com" with password "password" and I am user "user"
    When I edit the dealership with name "The Tavern"
      | shopName         |
      | Concesionario         |
    Then I'm viewing the details page for dealership by "test@test.com"
      | shopName       |
      | Concesionario  |
    And There are 1 dealerships

  Scenario: Try to edit restaurant but not logged in
    Given  I login as user "customer@customer.com" with password "password" and I am user "customer"
    When I list dealerships
    Then There is not "Editar" link available

  Scenario: Try to edit dealership but not logged in
    Given I'm not logged in
    When I list dealerships
    Then There is not "Editar" link available

#  Scenario: Try to edit restaurant but not the owner no edit button
#    Given I login as user "user2" with password "password"
#    When I view the details for restaurant "The Tavern"
#    Then There is no "Edit" link available
#
#  Scenario: Force edit restaurant but not the owner permission exception
#    Given I login as user "user2" with password "password"
#    When I edit the restaurant with name "The Tavern"
#      | country         |
#      | England         |
#    Then Server responds with page containing "403 Forbidden"
#    When I view the details for restaurant "The Tavern"
#    Then I'm viewing the details page for restaurant by "user1"
#      | name            | city            | country         |
#      | The Tavern      | London          | USA             |