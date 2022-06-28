# В этой задаче вам необходимо воспользоваться уже готовой функцией gcd(a, b),
# которая принимает два числа и находит наибольших общий делитель для них.
#
# Ваша задача при помощи функции gcd определить НОД произвольного количества чисел.
#
# Входные данные
# На первой строке вводится натуральное число n – количество чисел.
# Далее идут n строк, в каждой из которых натуральное число.
#
# Входные данные
# НОД введенных чисел.

# var1

from functools import reduce

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
s = [int(input()) for i in range(n)]
print(reduce(gcd, s))


# var2

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
num = int(input())
for i in range(1, n):
    num = gcd(num, int(input()))
print(num)
