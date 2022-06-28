def multiply(value):

    def inner(a):
        return value * a

    return inner


a2 = multiply(2)
print(a2(15))
