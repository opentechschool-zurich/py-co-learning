# roli's permutations generator translated from kotlin to python

def get_permutations(values, repeat):
    n = len(values)
    for i in range(pow(n, repeat)):
        permutation = []
        for j in range(repeat):
            permutation.append(values[i % n])
            i //= n
        yield permutation

def main():
    for p in get_permutations(['+', '-', '/', '%'], 3):
        print(p)

if __name__ == "__main__":
    main()

