# Найдите сумму всех четырехзначных чисел, сумма цифр каждого из которых равна 20.

# a = []
# for i in range(1000, 10000):
#     x = i
#     s = 0
#     while x > 0:
#         s += x % 10
#         x //= 10
#     if s == 20:
#         a.append(i)
# print(sum(a))
# ...or...
# s = 0
# for i in range(1000, 10000):
#     if sum(map(int, str(i))) == 20:
#         s += i
# print(s)


# В этой задаче вам предстоит построить лесенку из чисел. Программа принимает на вход
# целое положительное число n (n<=15) - количество уровней, ваша задача вывести n уровней,
# в каждом из которых стоят числа от 1 до значения уровня.

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()
# ...or...
# n=int(input())
# for i in range(1,n+1):
#     print(*range(1,i+1))
# ...or...
# [print(*[j+1 for j in range(i)]) for i in range(1, int(input())+1)]


