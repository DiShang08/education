# При помощи list comprehension создайте список, состоящий из первых n заглавных
# букв английского алфавита ['A', 'B', 'C', 'D', ...].
# Получить все заглавные буквы английского алфавита можно следующим образом:
#
# from string import ascii_uppercase
# print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Входные данные
# На вход программе подается натуральное число n, n≤26.#
# Формат выходных данных
# Программа должна вывести список из первых n заглавных букв английского алфавита

from string import ascii_uppercase
# print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
n = int(input())
print([ascii_uppercase[i] for i in range(n)])
