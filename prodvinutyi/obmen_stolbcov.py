#1
n, m = int(input()), int(input())
a = []
b = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
i, j = map(int, input().split())
for k in range(len(a)):
    a[k][i], a[k][j] = a[k][j], a[k][i]
for elem in a:
    print(*elem)

#2
n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
col1, col2 = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

for row in matrix:
    print(*row)
