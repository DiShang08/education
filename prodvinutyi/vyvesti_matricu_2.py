n, m = int(input()), int(input())
a = []
for _ in range(n):
    b = []
    for i in range(m):
        b.append(input())
    a.append(b)
# for i in a:
#     print(*i)
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
print()
for j in range(m):
    for i in range(n):
        print(a[i][j], end=' ')
    print()
