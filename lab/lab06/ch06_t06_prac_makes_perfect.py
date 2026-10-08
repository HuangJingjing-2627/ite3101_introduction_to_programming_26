from typing import Any


def cube(number: int) -> int:
    return number * number * number 

def cube(number: int) -> int:
    if number % 3 ==0:
        return cube(number)
    else:
        return False