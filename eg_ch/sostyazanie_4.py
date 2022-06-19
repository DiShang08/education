# В метании молота состязается n спортcменов. Каждый из них сделал m бросков.
# Победитель определяется по лучшему результату. Определите количество участников
# состязаний, которые разделили первое место, то есть определите количество
# строк в массиве, которые содержат значение, равное наибольшему.
# Входные данные
# Программа получает на вход два числа n и m, являющиеся числом строк и
# столбцов в массиве. Далее во входном потоке идет n строк по m чисел,
# являющихся элементами массива.
# # Выходные данные
# # Программа должна вывести  одно число - количество победителей соревнования.

# Variant_1

n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    max_res = 0
    for j in range(m):
        if a[i][j] > max_res:
            max_res = a[i][j]
    b.append(max_res)
print(b.count(max(b)))

# Variant_2

n, m = map(int, input().split())
a = [max(list(map(int, input().split()))) for i in range(n)]
print(a.count(max(a)))
