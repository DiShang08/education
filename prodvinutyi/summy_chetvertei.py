n = int(input())
a = []
b = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
lev, verh, prav, niz = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if j < i < n - 1 - j:
            lev += a[i][j]
        elif i < j and i < n - 1 - j:
            verh += a[i][j]
        elif j > i > n - 1 - j:
            prav += a[i][j]
        elif i > j and i > n - 1 - j:
            niz += a[i][j]
print(
    f'Верхняя четверть: {verh}\nПравая четверть: {prav}\nНижняя четверть: {niz}\nЛевая четверть: {lev}')
