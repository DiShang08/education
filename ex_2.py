# name = input()
# age = int(input())
# print(f"Hello {name.upper()}. You are {age} years old.")


# name = input()
# year = int(input())
# print(f"{name}, вам исполнится 77 лет в {year + 77}")


# sec = int(input())
# print(f"{sec} сек - это {sec // 60} мин. {sec % 60} сек.")


# w, h = map(int, input().split())
# print(f"""Разрешение экрана: {w} x {h}.
# Общее количество пикселей = {w * h}.""")


# a = int(input())
# b = int(input())
# print(f"""{a} / {b} = {a / b}
# {a} // {b} = {a // b}
# {a} % {b} = {a % b}""")


# x = int(input())
# y = int(input())
# z = int(input())
# print(f"""Vector A({x}, {y}, {z})
# Vector B({x + 5}, {y + 5}, {z + 5})""")


# kurs = float(input())
# kol = int(input())
# print(f"""Current dollar rate is {kurs}. You want buy {kol} dollars
# You must pay {kurs * kol}""")

# a = list(input().upper())
# a = '-'.join(a)
# a = a.replace('- -', ' ')
# print(a)


# a = input().split()
# # print(*a, sep='\n')
# print('\n'.join(a))


# a = input().split()
# io = []
# f = a[2]
# io.append(list(a[0])[0])
# io.append(list(a[1])[0])
# io = '.'.join(io) + '.'
# print(f, io)
#
# a = input().split()
# print(f'{a[-1]} {a[0][0]}.{a[1][0]}.')


# a = int(input())
# b = int(input())
# c = int(input())
# if (a + b) > c and (a + c) > b and (b + c) > a:
#     print('YES')
# else:
#     print('NO')


# a = input().rjust(6, '0')
# a_l = int(a[0]) + int(a[1]) + int(a[2])
# a_r = int(a[3]) + int(a[4]) + int(a[5])
# if a_l == a_r:
#     print('YES')
# else:
#     print('NO')


# s = '_abcdefgh'
# k1, k2 = input(), input()
# b1, b2 = k1[0], k2[0]
# stb1, stb2 = s.find(b1), s.find(b2)
# str1, str2 = int(k1[1]), int(k2[1])
# if (str1 + stb1) % 2 == 0 and (str2 + stb2) % 2 == 0 or (str1 + stb1) % 2 == 1 and (str2 + stb2) % 2 == 1:
#     print("YES")
# else:
#     print("NO")

# s = 'abcdefgh'
# a = input()
# b = input()
# a1 = (s.index(a[0]) + int(a[1])) % 2
# b1 = (s.index(b[0]) + int(b[1])) % 2
# if a1 == b1:
#     print("YES")
# else:
#     print("NO")

# print(('YES', 'NO')[sum(map(ord, input() + input())) % 2])


# n = int(input())
# if n % 2 == 0:
#     print(int(n / 2))
# else:
#     print(n // - 2)


# a, b = int(input()), int(input())
# if a != b:
#     if a < b:
#         print("<")
#     else:
#         print(">")
# else:
#     print("=")


# n = int(input())
# if n % 2 == 0:
#     print(n // 2)
# else:
#     if n == 1:
#         print(0)
#     else:
#         print(n)
