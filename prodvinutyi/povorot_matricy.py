n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n-1, -1, -1):
        print(a[j][i], end=' ')
    print()
