def fizzbuzz(number: int) -> str:
    fizz_num = 3
    buzz_num = 5
    ret = ""

    if number % fizz_num == 0:
        ret += "fizz"

    if number % buzz_num == 0:
        ret += "buzz"

    return ret
