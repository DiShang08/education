# Проверьте, является ли двумерный массив симметричным относительно главной
# диагонали. Главная диагональ — та, которая идёт из левого верхнего угла
# двумерного массива в правый нижний.
#
# Входные данные
#
# Программа получает на вход число n<100, являющееся числом строк и столбцов
# в массиве. Далее во входном потоке идет n строк по n чисел,
# являющихся элементами массива.
#
# Выходные данные
#
# Программа должна выводить слово Yes для симметричного массива и слово
# No для несимметричного.

# Variant_1
#
# n = int(input())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# flag = False
# for i in range(n):
#     for j in range(n):
#         if a[i][j] != a[j][i]:
#             flag = True
#             break
#     if flag:
#         print("No")
#         break
#     else:
#         print("Yes")
#         break
#
# Variant_2
#
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
count = 0
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            count += 1
if count > 0:
    print("No")
else:
    print("Yes")


