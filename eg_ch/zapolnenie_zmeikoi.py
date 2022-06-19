# Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).
#
# Входные данные
# Программа получает на вход два числа n и m.
#
# Выходные данные
# Программа должна вывести  полученный массив, при этом между числами
# может быть любое количество пробелов.

# var_1

n, m = map(int, input().split())
a = [[str(j + i * m) for j in range(m)] for i in range(n)]
for i in range(1, n, 2):
    a[i] = a[i][::-1]
for i in a:
    print(' '.join(i))

# var_2

n, m = map(int, input().split())
for i in range(n):
    a = []
    for j in range(m):
        a.append(j + i * m)
    if i % 2 != 0:
        a = a[::-1]
    print(*a)
