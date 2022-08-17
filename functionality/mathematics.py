import math


def is_prime(input_value: int) -> bool:
    if input_value <= 1:
        return False

    if input_value.__class__ != int:
        return False

    for i in range(2, int(math.sqrt(input_value))+1):
        if input_value % i == 0:
            return False

    return True
