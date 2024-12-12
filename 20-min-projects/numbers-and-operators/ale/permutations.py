# roli's permutations generator translated from kotlin to python

def get_permutations(values, repeat):
    n = len(values)
    for i in range(pow(n, repeat)):
        permutation = []
        quotient = i
        for j in range(repeat):
            # combine modulo and floor division for increasing permutations
            # see https://docs.python.org/3/glossary.html#term-floor-division
            permutation.append(values[quotient % n])
            quotient //= n
        # make this function a generator by returning an iterator
        # see https://docs.python.org/3/glossary.html#term-generator
        yield permutation

def main():
    for p in get_permutations(['+', '-', '/', '%'], 3):
        print(p)

if __name__ == "__main__":
    main()

