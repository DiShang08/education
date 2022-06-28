def adder(value):

    def inner(a):
        return value + a

    return inner


a2 = adder(2)
print(a2(5))
