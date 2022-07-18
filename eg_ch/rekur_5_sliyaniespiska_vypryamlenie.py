def flatten(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        return(flatten(s[0]) + flatten(s[1:]))
    return(s[:1] + flatten(s[1:]))


s = [[1, 2], [3, 4]]
print("Выпрямленный список: ", flatten(s))
s = ([1, [2, 3, [4]], 5])  # вернет [1,2,3,4,5]
print("Выпрямленный список: ", flatten(s))
s = ([1, [2, 3], [[2], 5], 6])  # вернет [1,2,3,2,5,6]
print("Выпрямленный список: ", flatten(s))
s = ([[[[9]]], [1, 2], [[8]]])  # вернет [9,1,2,8]
print("Выпрямленный список: ", flatten(s))
