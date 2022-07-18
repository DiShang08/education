# Входные данные состоят из пяти строк, в каждой из которых записаны пять целых
# чисел: j-ое число в i-ой строке входных данных обозначает элемент матрицы,
# стоящий на пересечении i-ой строки и j-ого столбца. Гарантируется,
# что матрица состоит из 24-x нулей и единственной единицы.
# Выведите единственное целое число — минимальное количество действий,
# которое требуется, чтобы сделать матрицу красивой - если единственная
# единица этой матрицы будет находиться в ее центре.

# a = []
# for i in range(5):
#     a.append(list(map(int, input().split())))
# # ind = [item for sublist in a for item in sublist].index(1)
# ind = []
# for i in a:
#     for n in i:
#         ind.append(n)
# ind = ind.index(1)
# x = ind // 5
# y = ind % 5
# print(abs(2 - y) + abs(2 - x))
#
# ...or...

a = []
for i in range(5):
    a.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            print((abs(2-i))+(abs(2-j)))
            break
