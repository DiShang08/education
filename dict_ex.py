from string import ascii_lowercase
dicts = {}
dd = []
d = ascii_lowercase
for i in d:
    dd.append(i)
keys = range(1, 27)
values = [i for i in range(1, len(keys) + 1)]
for i in keys:
    dicts[i] = dd[i-1]
print(dicts)
