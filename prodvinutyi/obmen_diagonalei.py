# 1
n = int(input())
a = []
b = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for j in range(n):
        if (i == j) or (i == n-1-j):
            print(a[n-1-i][j], end=' ')
        else:
            print(a[i][j], end=' ')
    print()

# 2
n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for row in matrix:
    print(*row)

# 3
