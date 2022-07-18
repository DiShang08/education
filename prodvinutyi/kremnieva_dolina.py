import re
n = int(input())
count = 0
h = []
for i in range(n):
    b = ''
    a = input()
    count += 1
    for j in 'anton':
        if j in a:
            b += j
            a = a[a.find(j):]
    if b == 'anton':
        h.append(count)
print(*h)

# 2  с помощью регулярных выражений

num = int(input())
for i in range(num):
    if re.search(r'.*a.*n.*t.*o.*n', input()):
        print(i + 1, end=' ')
