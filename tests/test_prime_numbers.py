import pytest
from functionality.mathematics import *


@pytest.mark.parametrize("input_value", [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 21, 25, 27])
def test_should_return_false_for_non_prime_inputs(input_value):
    assert is_prime(input_value) is False


@pytest.mark.parametrize("input_value", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
def test_should_return_true_for_prime_inputs(input_value):
    assert is_prime(input_value) is True
