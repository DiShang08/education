# ex1
# def hero(bullets, dragons):
#     if dragons == 0 or bullets / dragons >= 2:
#         return True
#     else:
#         return False


# print(hero(2, 1))


# ex2
# var1
# def count_sheep(n):
#     res = ""
#     for i in range(1, n+1):
#         res += str(i)+' sheep...'
#     return res
# var2
# def count_sheep(n):
#     return ''.join(f"{i} sheep..." for i in range(1, n+1))


# n = int(input())
# print(count_sheep(n))


# ex3
# def better_than_average(class_points, your_points):
#     return your_points > (sum(class_points)/len(class_points))


# print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))
# print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))


# ex4
# var1
# def positive_sum(arr):
#     pos_sum = 0
#     for i in arr:
#         if i > 0:
#             pos_sum += i
#     return pos_sum
# # var2
# def positive_sum1(arr):
#     return sum(i for i in arr if i > 0)


# ex5
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg*fuel_left >= distance_to_pump


print(zero_fuel(60, 25, 2))
