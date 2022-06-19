s = input()
count = 0
while "Р" * (count + 1) in s:
    count += 1
print(count)

# 2

#s = input()
print(max(map(len, input().split('О'))))

# 3

stroka = input().split('О')
r = max(stroka, key=len)
print(len(r))
