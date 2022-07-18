n, m = int(input()), int(input())
a = []
for _ in range(n):
    b = []
    for i in range(m):
        b.append(input())
    a.append(b)
for i in a:
    print(*i)
