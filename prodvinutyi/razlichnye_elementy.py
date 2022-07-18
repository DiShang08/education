a = input().split()
s = []
for i in a:
    if i not in s:
        s.append(i)
print(len(s))
