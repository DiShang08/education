my_tuple = (
-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593,
905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829,
-275, 619, -628, -241, -565, -835, -69,
747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562,
333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422,
-895, 198, 284, 472, -986, -964, -73, 29)
print(min(my_tuple), max(my_tuple))
print(sum(my_tuple) / len(my_tuple))
odd, odd_count = 0, 0
for i in my_tuple:
    if i % 2 != 0:
        odd += i
        odd_count += 1
print(odd / odd_count)

a, b = int(input()), int(input())
# s = []
# for i in range(a, b+1):
#     s.append(i)
# print(tuple(s))
s = [i for i in range(a, b + 1)]
print(tuple(s))

n = int(input())
# s = []
# for i in range(n, n**2 + 1):
#     if i % 2 != 0:
#         s.append(i)
s = [i for i in range(n, n ** 2 + 1) if i % 2 != 0]
print(tuple(s))
print(tuple(i for i in range(n, n ** 2 + 1) if i % 2 != 0))
