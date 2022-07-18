# 1
n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))
boys.sort()
girls.sort()
count = 0
i, j = 0, 0
while i < n and j < m:
    if abs(boys[i]-girls[j]) <= 1:
        count += 1
        i += 1
        j += 1
    elif boys[i] < girls[j]:
        i += 1
    else:
        j += 1
print(count)


# 2
n = int(input())
lst1 = sorted(list(map(int, input().split())))
m = int(input())
lst2 = sorted(list(map(int, input().split())))
count = 0
while lst1 and lst2:
    if abs(lst2[-1] - lst1[-1]) < 2:
        count += 1
        lst1.pop()
        lst2.pop()
    elif lst1[-1] > lst2[-1]:
        lst1.pop()
    else:
        lst2.pop()
print(count)
