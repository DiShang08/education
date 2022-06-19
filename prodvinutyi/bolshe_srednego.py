n = int(input())
a = []
s = 0
b = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
# 1
# for i in range(n):
#     counter = 0
#     for j in range(n):
#         s += a[i][j]
#     sr = s/n
#     for j in range(n):
#         if a[i][j] > sr:
#             counter += 1
#     print(counter)
#     s = 0
# 2
for i in range(n):
    counter = 0
    sr = sum(a[i])/n
    for j in range(n):
        if a[i][j] > sr:
            counter += 1
    print(counter)
