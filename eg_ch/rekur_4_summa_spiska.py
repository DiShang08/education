# 1
# def list_sum_recursive(s):
#     if len(s) == 0:
#         return 0
#     return s.pop() + list_sum_recursive(s)
#
#
# s = [1, 2, 3]
# print(list_sum_recursive(s))

# 2
def list_sum_recursive(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return s[0]
    return s[0] + list_sum_recursive(s[1:])


s = [1, 2, 3]
print(list_sum_recursive(s))
