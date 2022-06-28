# Напишите функцию factorial, которая принимает на вход одно неотрицательное
# число, и возвращает значение факториала данного числа.
#
# Нужно определить только функцию

def factorial(n):
    pr=1
    for i in range(2, n+1):
        pr *=i
    return pr

# n = int(input())
# print(factorial(n))

