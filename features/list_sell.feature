Feature: List Sells
  I want to see the sell's list


  Background: There are 6 registered Cars
    Given Exists a user "test" with password "test" and email "test@test.com" with Seller role
    Given Exists a user "customer" with password "customer" and email "customer@customer.com" with Customer role
    And Exists cars registered
    | name            |
    | troncomovil     |
    | audimusprime    |
    | La furia        |
    | clio del radu   |
    | fiesta del luis |
    | Barco de guerra |
    And all of them are sold by user "test@test.com"
    | name            |
    | troncomovil     |
    | audimusprime    |
    | La furia        |
    | clio del radu   |
    | fiesta del luis |
    | Barco de guerra |

  Scenario: List all the sells
    Given I login as user "test@test.com" with password "test" and I am user "test"
    When I list sells
    Then I'm viewing a list containing those sells by user "test"
    | name            |
    | troncomovil     |
    | audimusprime    |
    | La furia        |
    | clio del radu   |
    | fiesta del luis |
    | Barco de guerra |
    And list contains 6 sells


  Scenario: List all the sells without being a Seller
    Given I login as user "customer@customer.com" with password "customer" and I am user "customer"
    When I list sells
    Then list contains 0 sells





