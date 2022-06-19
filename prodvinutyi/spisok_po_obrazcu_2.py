n = int(input())
# var1
result = []
for i in range(1, n+1):
    result.append(list(range(1, i + 1)))
# var2
list1 = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]

print(*result, sep='\n')
print(*list1, sep='\n')
