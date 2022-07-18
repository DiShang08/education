# Давайте усовершенствуем предыдущую задачу так, чтобы получался следующий список букв:
# # ['A', 'BB', 'CCC', 'DDDD', 'EEEEE', 'FFFFFF', ...]
# Входные данные
# На вход программе подается натуральное число n, n ≤ 26.
# # Формат выходных данных
# Программа должна вывести список из первых n заглавных букв английского алфавита
# , причем каждая буква должна быть продублирована в зависимости от своего
# порядкового номера

from string import ascii_uppercase
n = int(input())
print([ascii_uppercase[i] * (i + 1) for i in range(n)])