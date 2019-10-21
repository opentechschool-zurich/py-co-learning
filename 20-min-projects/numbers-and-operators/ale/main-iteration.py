# 1 ? 2 ? 3 ? 4 == 24
# 1 * 2 * 3 * 4 == 24

import itertools
values = [1,2,3,4]
total = 24

ACTIONS = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}

# all permuatations n times
for operators in itertools.product(ACTIONS.keys(), repeat=len(values) - 1):
    # print(operators)
    result = values[0]
    values_lowpriority = []
    operators_lowpriority = []
    for o, n in zip(operators, values[1:]):
        if o in ['*', '/']:
            result = ACTIONS[o](result, n)
        else:
            values_lowpriority.append(result)
            operators_lowpriority.append(o)
            result = n
    if values_lowpriority:
        values_lowpriority.append(result)
        result = values_lowpriority[0]
        for o, n in zip(operators_lowpriority, values_lowpriority[1:]):
            result = ACTIONS[o](result, n)

    if result == total:
        print(operators)
