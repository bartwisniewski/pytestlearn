import pytest
from functionality.fizzbuzz import *


def get_fizz_nums():
    ret = []
    for i in range(3, 100, 3):
        if i % 5 != 0:
            ret.append(i)
    return ret


@pytest.fixture()
def get_buzz_nums():
    ret = []
    for i in range(5, 100, 5):
        if i % 3 != 0:
            ret.append(i)
    return ret


@pytest.fixture()
def get_fizzbuzz_nums():
    ret = []
    for i in range(5, 100, 5):
        if i % 3 == 0:
            ret.append(i)
    return ret


@pytest.fixture()
def get_other_nums():
    ret = []
    for i in range(0, 100, 1):
        if i % 3 != 0 and i % 5 != 0:
            ret.append(i)
    return ret


@pytest.mark.parametrize("num", get_fizz_nums())
def test_should_return_fizz_for_multiplications_of_3(num):
    assert fizzbuzz(num) == "fizz"


def test_should_return_buzz_for_multiplications_of_5(get_buzz_nums):
    for num in get_buzz_nums:
        assert fizzbuzz(num) == "buzz"


def test_should_return_fizzbuzz_for_multiplications_of_3_and_5(get_fizzbuzz_nums):
    for num in get_fizzbuzz_nums:
        assert fizzbuzz(num) == "fizzbuzz"


def test_should_return_emptystring_for_other_numbers(get_other_nums):
    for num in get_other_nums:
        assert fizzbuzz(num) == ""


def test_should_return_fizzbuzz_for_0():
    assert fizzbuzz(0) == ""
