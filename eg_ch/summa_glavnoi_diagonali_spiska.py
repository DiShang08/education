# Вам нужно посчитать сумму элементов двумерного квадратного (NxN) списка,
# которые расположены на главной диагонали.
#
# Под главной диагональю матрицы подразумевается диагональ, проведённая
# из левого верхнего угла в правый нижний.
#
# Программа сперва принимает на вход число N (N<=15) -
# количество строк и столбцов в списке, а затем в N строках записаны элементы списка.

n = int(input())    # количество строк и столбцов матрицы
a = []
s = 0
for i in range(n):
    a.append(list(map(int, input().split())))    # заполнение списка
    for j in range(n):    # обход столбцов матрицы
        if i == j:        # если текущий элемент находится на главной диагонале
            s += a[i][j]  # суммирование элемента
print(s)
