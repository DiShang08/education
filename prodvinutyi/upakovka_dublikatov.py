s = input().split()
li = []
for i in s:
    if li and i in li[-1]:
        li[-1].append(i)
    else:
        li.append([i])
print(li)

# for i in s:
#     if i not in li[-1]:
#         li.append([i])
#     else:
#         li[-1].append(i)
# print(li)
