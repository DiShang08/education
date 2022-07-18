n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
pr = int(input())
res = "НЕТ"
for i in range(n):
    for j in range(n):
        if i != j:
            if s[i] * s[j] == pr:
                res = "ДА"
                break
print(res)
