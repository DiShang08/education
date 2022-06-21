# 1
# def hero(bullets, dragons):
#     if dragons == 0 or bullets / dragons >= 2:
#         return True
#     else:
#         return False


# print(hero(2, 1))


# 2
# var1
def count_sheep(n):
    res = ""
    for i in range(1, n+1):
        res += str(i)+' sheep...'
    return res
# var2
# def count_sheep(n):
#     return ''.join(f"{i} sheep..." for i in range(1, n+1))


n = int(input())
print(count_sheep(n))
