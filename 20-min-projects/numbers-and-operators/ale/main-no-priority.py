# 1 ? 2 ? 3 ? 4 == 24
# 1 * 2 * 3 * 4 == 24

import itertools
values = [1,2,3,4]
total = 24

ACTIONS = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
# print(ACTIONS['+'](1, 2))

# all permutations n times
for operators in itertools.product(ACTIONS.keys(), repeat=len(values) - 1):
    # print(operators)
    result = values[0]
    for o, n in zip(operators, values[1:]):
        result = ACTIONS[o](result, n)
    if result == total:
        print(operators)
        print(result)
