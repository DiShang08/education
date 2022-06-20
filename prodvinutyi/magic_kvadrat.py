n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
flag = "YES"
first = sum(matrix[0])
digits = [i for i in range(1, n ** 2 + 1)]

for i in range(1, n):
    if sum(matrix[0]) != first:
        flag = "NO"
        break
for i in range(n):
    for j in range(n):
        if matrix[i][j] in digits:
            digits.remove(matrix[i][j])
    if i == n - 1 and j == n - 1 and digits != []:
        flag = 'NO'

for j in range(n):
    result = 0
    for i in range(n):
        result += matrix[i][j]
        if i == n - 1 and result != first:
            flag = 'NO'
            break

print(flag)
