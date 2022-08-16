from random import random
import pytest
from typing import List
from functionality.quicksort import *


@pytest.fixture()
def gen_random_list() -> List[float]:
    length = 10000
    max_value = 10 ** 3
    list_of_randoms = []
    for i in range(0, length):
        list_of_randoms.append(random()*max_value)
    return list_of_randoms


def test_should_be_in_right_order(gen_random_list):
    test_list = gen_random_list
    quicksort(test_list)
    is_valid = True
    last_val = test_list[0]
    for float_val in test_list[1:]:
        if float_val < last_val:
            is_valid = False
            break
        last_val = float_val

    assert is_valid


def test_should_raise_no_error_for_empty_list():
    quicksort([])


def test_should_do_nothing_for_single_element_list():
    test_list = [5]
    quicksort(test_list)
    assert test_list[0] == 5 and len(test_list) == 1


def test_should_do_nothing_for_same_elements_list():
    test_list = [5, 5, 5, 5]
    quicksort(test_list)
    assert test_list[0] == 5 and len(test_list) == 4
