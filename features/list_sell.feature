Feature: List Sells
  I want to see the sell's list


  Background: There are 6 registered Cars
    Given Exists a user "test" with password "test" and email "test@test.com" with Seller role
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
    When I list sells
    Then I'm viewing a list containing those sells
    | name            |
    | troncomovil     |
    | audimusprime    |
    | La furia        |
    | clio del radu   |
    | fiesta del luis |
    | Barco de guerra |
    And list contains 6 sells






