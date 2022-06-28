# Замыкания

def main_func(name):
    def inner_func():
        print('hello my friend', name)

    return inner_func


i = main_func('Ivan')
i()
