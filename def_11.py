# В этой задаче вам необходимо воспользоваться уже готовой функцией factorial,
# которая принимает неотрицательное число, и возвращает значение факториала
# данного числа.
#
# Ваша задача создать функцию trailing_zeros, которая принимает неотрицательное
# число, находит его факториал и возвращает сколько нулей на конце этого факториала .
#
# trailing_zeros(6) # возвращает "1" потому что 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
# trailing_zeros(10) # возвращает 2 потому что 10! = 3 628 800
# trailing_zeros(20) # возвращает 4 потому что 20! = 2 432 902 008 176 640 000
#
# Нужно написать только определение функций trailing_zeros и factorial

def factorial(n: int):
    pr = 1
    for i in range(2, n + 1):
        pr *= i
    return pr

def trailing_zeros(n: int) -> int:
    n = factorial(n)
    n = str(n)
    return (len(n) - len(n.rstrip('0')))

# n = 6
# print(trailing_zeros(n))
