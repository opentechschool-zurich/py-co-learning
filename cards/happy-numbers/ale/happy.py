happy = []

def is_happy(number):
    global loop
    nstring = str(number)
    sumsquare = 0
    for c in nstring:
        # print(c)
        sumsquare += int(c) ** 2
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
