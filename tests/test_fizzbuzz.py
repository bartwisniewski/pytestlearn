from functionality.fizzbuzz import *
from pytest_bdd import scenario, given, when, then


@scenario('fizzbuzz.feature', 'Fizz number')
def test_fizz():
    pass


@scenario('fizzbuzz.feature', 'Buzz number')
def test_buzz():
    pass


@scenario('fizzbuzz.feature', 'Fizzbuzz number')
def test_fizzbuzz():
    pass


@given("I have a number which is divider of 3 and not of 5", target_fixture="number")
def divider_of_3():
    return 6


@given("I have a number which is divider of 5 and not of 3")
def divider_of_5():
    return 10


@given("I have a number which is divider of 3 and of 5")
def divider_of_3_5():
    return 15


@when("when I run fizzbuzz game", target_fixture="fizzbuzz_return")
def fizzbuzz_game(number: int):
    return fizzbuzz(number)


@then('Then I should see {expexted} printed')
def test_fizzbuzz_return(expected, fizzbuzz_return):
    assert fizzbuzz_return == expected
