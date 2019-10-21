# 1 ? 2 ? 3 ? 4 == 24
# 1 * 2 * 3 * 4 == 24

from itertools import product

ACTIONS = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}

def calculate(operators, result, values):
    if not operators:
        return result

    if operators[0] in ['*', '/']:
        return calculate(operators[1:], ACTIONS[operators[0]](result, values[0]), values[1:])

    return ACTIONS[operators[0]](result, calculate(operators[1:], values[0], values[1:]))

def find_permutations(values, total):
    return [permutation for permutation in
            product(ACTIONS.keys(), repeat=len(values) - 1) if
            calculate(permutation, values[0], values[1:]) == total]

def main():
    print(find_permutations([1, 2, 3, 4], 24))

def test():
    if calculate([], 0, 0) != 0: print('fail 0')
    if calculate(['*'], 2, [3]) != 6: print('fail 2 * 3')
    if calculate(['*', '*'], 2, [3, 4]) != 24: print('fail 2 * 3 * 4')
    if calculate(['+'], 2, [3]) != 5: print('fail 2 + 3')
    if calculate(['+', '+'], 2, [3, 4]) != 9: print('fail 2 + 3 + 4')
    if calculate(['*', '+'], 2, [3, 4]) != 10: print('fail 2 + 3 + 4')
    if calculate(['+', '*'], 2, [3, 4]) != 14: print('fail 2 + 3 + 4')

if __name__ == "__main__":
    main()
    # test()
