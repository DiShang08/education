# s, v1, v2, t1, t2 = map(int, input().split())
# f1 = s * v1
# f2 = s * v2
# T1 = 2 * t1 + f1
# T2 = 2 * t2 + f2
# if T1 != T2:
#     if T1 < T2:
#         print("First")
#     else:
#         print("Second")
# else:
#     print("Friendship")


# a = input().lower()
# b = input().lower()
# if a[-1] != 'ь':
#     if a[-1] == b[0]:
#         print("Good")
#     else:
#         print("Bad")
# else:
#     if a[-2] == b[0]:
#         print("Good")
#     else:
#         print("Bad")


# a, b = map(int, input().split())
# h = 0
# while a != 0:
#     a -= 1
#     h += 1
#     if h % b == 0:
#         a += 1
# print(h)


# n = int(input())
# n1 = int(str(n)[0])
# while n1 != 1 and n <= 10 ** 9:
#     n *= n1
#     n1 = int(str(n)[0])
# print(n)


# i = 0
# while i < 5:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Конец")


# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# print(i)


# n = int(input())
# i = 2
# while True:
#     if n % i == 0:
#         break
#     i += 1
# print(i)


# a = int(input())
# b = int(input())
# while a <= b:
#     if a % 777 == 0:
#         break
#     elif a % 2 == 0 or a % 3 == 0:
#         a += 1
#         continue
#     print(a)
#     a += 1


# n = int(input())
# c = 0
# while True:
#     if n % 2 == 0:
#         n = n / 2
#     else:
#         n = 3 * n + 1
#     c += 1
#     if n == 1:
#         break
# print(c)


# a = input()
# i = 0
# while i < len(a):
#     if a[i] in 'ea':
#         print("Ага! Нашлась")
#         break
#     print("Текущая буква:", a[i])
#     i += 1
# else:
#     print("Распечатали все буквы")


# def say_hello_world(name):
#     print(f'{name} говорит hello world!')


# name = input()
# say_hello_world(name)
# my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
# print(my_tuple.count(50))