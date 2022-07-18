n = int(input())
a = []
b = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
s = a[0][0]
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j) or (i == j) or (i + j + 1 == n):
            if a[i][j] > s:
                s = a[i][j]
print(s)
