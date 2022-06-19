n, m = int(input()), int(input())
b = []
for i in range(n):
    mult = []
    for j in range(m):
        mult.append(str(i*j).ljust(3))
    print(*mult)

# 2
n, m = int(input()), int(input())
mult = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()

# 3
m, n = int(input()), int(input())
mult = [[i*j for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()
