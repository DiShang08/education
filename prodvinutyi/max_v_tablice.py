n, m = int(input()), int(input())
a = []
b = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)

#1
m = max(max(a, key=max))
for i in range(n):
    if m in a[i]:
        print(i, a[i].index(m))
        break
#2
m = max(a, key=max)
print(a.index(m), m.index(max(m)))

#3
n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row,col = i, j

print(row, col)
