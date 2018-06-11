from typing import List

happy: List[int] = []
# [1, 7, 10, 13, 19, 23, 28, 31]


def get_digits(number):
    result = []
    while (number > 0):
        d = number % 10
        result.append(d)
        number -= d
        number //= 10
    return list(reversed(result))
        
def is_happy(number, cycle: List=None):
    if cycle is None:
        cycle = []
    if number in cycle:
        return False
    else:
        cycle.append(number)
    sumsquare = 0
    for d in get_digits(number) :
        sumsquare += int(d) ** 2
    if sumsquare != 1:
        return is_happy(sumsquare, cycle)
    return True

i = 1
while len(happy) < 8:
    if is_happy(i):
        happy.append(i)
    i += 1

print(happy)
