from typing import List


n = [3, 5, 7]

def total(number: List[int]) -> int:
    result = 0
    for number in number:
        result += number
    return result