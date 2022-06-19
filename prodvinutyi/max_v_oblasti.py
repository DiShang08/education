n = int(input())
a = []
b = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
s=a[0][0]
for i in range(n):
    for j in range(i+1):
        if a[i][j] > s:
            s = a[i][j]
print(s)
