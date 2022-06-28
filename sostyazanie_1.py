# Входные данные#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов
# в массиве. Далее во входном потоке идет n строк по m чисел,
# являющихся элементами массива.
# # Выходные данные
# # Программа должна вывести  2 числа: сумму и номер строки, для которой
# эта сумма достигается. Если таких строк несколько, то выводится номер
# наименьшей из них. Не забудьте, что нумерация строк (спортсменов) начинается с 0.

n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    a.append(list(map(int, input().split())))
    s = 0
    for j in range(m):
        s += a[i][j]
    b.append(s)
print(max(b), b.index(max(b)), sep='\n')