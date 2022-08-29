Feature: Fizzbuzz
    Fizzbuzz game

    Scenario: Fizz number
        Given I have a number which is divider of 3 and not of 5

        When I run fizzbuzz game

        Then I should see fizz printed


    Scenario: Buzz number
        Given I have a number which is divider of 5 and not of 3

        When I run fizzbuzz game

        Then I should see buzz printed


    Scenario: Fizzbuzz number
        Given I have a number which is divider of 3 and of 5

        When I run fizzbuzz game

        Then I should see fizzbuzz printed
