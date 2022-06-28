# В метании молота состязается n спортcменов. Каждый из них сделал m бросков.
# Побеждает спортсмен, у которого максимален наилучший бросок.
# Если таких несколько, то из них побеждает тот, у которого наилучшая
# сумма результатов по всем попыткам. Если и таких несколько,
# победителем считается спортсмен с минимальным номером. Определите
# номер победителя соревнований.
# # Входные данные#
# Программа получает на вход два числа n и m, являющиеся числом строк и
# столбцов в массиве. Далее во входном потоке идет n строк по m чисел,
# являющихся элементами массива.
# # Выходные данные
# # Программа должна вывести одно число - номер победителя соревнований.
# Не забудьте, что  строки  (спортсмены) нумеруются с 0.

# Variant_1

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
max_score = 0
max_sum = 0
max_ind = 0
for i in range(n):
    max_try = 0
    s = 0
    for j in range(m):
        s += a[i][j]
        if a[i][j] > max_try:
            max_try = a[i][j]
    if max_try > max_score:
        max_score = max_try
        max_sum = s
        max_ind = i
    elif max_try == max_score and s > max_sum:
        max_score = max_try
        max_sum = s
        max_ind = i
print(max_ind)

# Variant_2

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
x = []
for i in range(n):
    x.append((max(a[i]), sum(a[i])))
print(x.index(max(x)))
