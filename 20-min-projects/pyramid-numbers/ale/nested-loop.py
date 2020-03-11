# print with nested loops:
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0

n = 4
for i in range(n + 1):
    for j in range(i + 1):
        print(j, end=' ')
    print()
for i in range(n, 0, -1):
    for j in range(i):
        print(j, end=' ')
    print()

print("----")

for i in range(-n, n + 1):
    # print(n - abs(n))
    for j in range(n - abs(i) + 1):
        print(j, end=' ')
    print()

print("----")

for i in range(n, -n - 1, -1):
    for j in range(n, abs(i) - 1, -1):
        print(n - j, end=' ')
    print()

print("----")
