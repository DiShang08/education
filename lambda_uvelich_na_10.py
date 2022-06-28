# def adding(x):
#     return lambda x: x + 10


# print(adding(10))

# # или просто переменная

# adding_10 = lambda x: x + 10
# print(adding_10)


def starts_with(s):
    return s.startswith('W')


s = input()
print(starts_with(s))
