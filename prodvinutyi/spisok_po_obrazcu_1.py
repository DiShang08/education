# n = int(input())
# for i in range(n):
#     my_list = []
#     for j in range(1, n+1):
#         my_list.append(j)
#     print(my_list, sep='\n')

n = int(input())
result = []
list1 = [[j for j in range(1, n + 1)] for i in range(1, n + 1)]
for _ in range(n):
    result.append(list(range(1, n + 1)))
print(*result, sep='\n')
print(*list1, sep='\n')
