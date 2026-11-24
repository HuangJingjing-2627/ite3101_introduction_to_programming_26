from typing import List
# Add your function here

n = [3, 5, 7]
# print(list_extender(n))


def list_extender(l: List[int]) -> List[int]:
    l.append(9)
    return l


print(list_extender(n))
print(n)
