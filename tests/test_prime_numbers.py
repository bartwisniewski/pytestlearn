import pytest
from functionality.mathematics import *


@pytest.mark.parametrize("input_value", [4, 6, 8, 9, 10, 12, 14, 15, 21, 25, 27])
def test_should_return_false_for_non_prime_inputs(input_value):
    assert is_prime(input_value) is False


@pytest.mark.parametrize("input_value", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
def test_should_return_true_for_prime_inputs(input_value):
    assert is_prime(input_value) is True


@pytest.mark.parametrize("input_value", [-4, -6, -8, -9])
def test_should_return_false_for_negative_inputs(input_value):
    assert is_prime(input_value) is False


@pytest.mark.parametrize("input_value", [0, 1])
def test_should_return_false_for_special_integers(input_value):
    assert is_prime(input_value) is False


@pytest.mark.parametrize("input_value", [3.5, 4.7, 11.767])
def test_should_return_false_for_floats(input_value):
    assert is_prime(input_value) is False


@pytest.mark.parametrize("input_value", [182765782, 29395758392, 292839371768])
def test_should_return_false_for_very_big_even(input_value):
    assert is_prime(input_value) is False
