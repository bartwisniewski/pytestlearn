

def is_prime(input_value: int) -> bool:
    if input_value in [0, 1]:
        return False

    for i in range(2, int(input_value / 2) + 1):
        if input_value % i == 0:
            return False

    return True
