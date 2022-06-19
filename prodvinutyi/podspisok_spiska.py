# 1

a = input().split()
dop, result = [], [[]]
for i in range(len(a)):
    for j in range(len(a)):
        dop = a[j:i+j+1]
        if len(dop) == i+1:
            result.append(dop)
print(result)

# 2

input_data = input().split()
output_data = [[]]
for i in range(len(input_data)):
    for j in range(len(input_data) - i):
        output_data.append(input_data[j: j + i + 1])
print(output_data)
