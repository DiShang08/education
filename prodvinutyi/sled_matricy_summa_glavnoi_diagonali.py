n = int(input())
a = []
s = 0
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             s += a[i][j]
# print(s)

for i in range(n):
    s += a[i][i]
print(s)
