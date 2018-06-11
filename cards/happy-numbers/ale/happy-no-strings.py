from typing import List

happy: List[int] = []

def get_digits(number):
    result = []
    while (number > 0):
        d = number % 10
        result.append(d)
        number -= d
        number //= 10
    return list(reversed(result))
        

print(get_digits(12))

def is_happy(number):
    global loop
    sumsquare = 0
    for d in get_digits(number) :
        sumsquare += int(d) ** 2
    if loop > 100:
        return False
    if sumsquare != 1:
        loop += 1
        sumsquare = is_happy(sumsquare)
    return loop < 100

i = 1
while len(happy) < 8:
    loop = 0
    if is_happy(i):
        happy.append(i)
    i += 1


print(happy)
