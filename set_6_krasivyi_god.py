# Кажется, еще совсем недавно наступил новый 2013 год. А знали ли Вы
#  забавный факт о том, что 2013 год является первым годом после
#  далекого 1987 года, в котором все цифры различны?

# Теперь же Вам предлагается решить следующую задачу:
#  задан номер года, найдите наименьший номер года, который
#  строго больше заданного и в котором все цифры различны.

# Входные данные
# В единственной строке задано целое число y (1000 ≤ y ≤ 9000)
#  — номер года.

# Выходные данные
# Выведите единственное целое число — минимальный номер года,
#  который строго больше y, в котором все цифры различны.
#  Гарантируется, что ответ существует.


# var_1_подробный вариант

y = int(input()) + 1
s = set()
for i in str(y):
    s.add(i)
while len(s) != 4:
    s = set()
    y += 1
    for i in str(y):
        s.add(i)
print(y)

# var_2_ сокращенный вариант

y = int(input()) + 1
while len(set(str(y))) != 4:
    y += 1
print(y)
