# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1)
# print(res)


# def func(num1, num2):
#     return num1 % num2 == 0


# num1 = int(input())
# num2 = int(input())
# print("делится" if func(num1, num2) else "не делится")

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for li in list1:
#     if max(li) > maximum:
#         maximum = max(li)
# print(maximum)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105],
#          [100, 99, 98, 103], [1, 2, 3]]
# for li in list1:
#     li.reverse()
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105],
#          [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for li in list1:
#     counter += sum(li)
#     total += len(li)
# print(counter/total)

# list1 = [[1, 2, 3], [4, 5]]
# list2 = list1
# list1[0].append(7)
# print(list2)

# list1 = [[1] * 3] * 3
# print(list1)
# list1[0][1] = 5
# print(list1)
# print(list1[1][1])

# n = 3
# list1 = []
# for _ in range(n):
#     row = input().split()
#     list1.extend(row)
# print(list1)

# my_list = [[1], [2, 3], [4, 5, 6]]
# total = 0

# for row in my_list:
#     total += sum(row)
# print(type(row))
# print(total)

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
# maximum = my_list[0][0]
# minimum = my_list[0][0]
# print(maximum, minimum)
# for row in my_list:
#     maximum = max(row)
#     minimum = min(row)
#     print(maximum, minimum)
# print(maximum + minimum)

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
# maximum = my_list[0][0]
# minimum = my_list[0][0]
# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)
# print(maximum + minimum)

