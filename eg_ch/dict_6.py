s = input().lower()
d = {}
for i in s:
    if i.isalpha():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
print(d)
