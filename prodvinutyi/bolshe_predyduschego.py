# s = [int(n) for n in input().split()]
s = list(map(int, input().split()))
count = 0
for i in range(1, len(s)):
    if s[i-1] < s[i]:
        count += 1
print(count)
