s = [int(n) for n in input().split()]
for i in range(0, len(s)-1, 2):
    s[i], s[i+1] = s[i+1], s[i]
# s[:-1:2], s[1::2] = s[1::2], s[:-1:2]
print(*s)
