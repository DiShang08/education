# var1
def func_show(func):
    def wrapper(*args):
        keys, values = func(*args)
        return dict(zip(keys, values))
        # return dict(zip(*func(*args)))
    return wrapper


@func_show
def get_list(line_keys, line_values):
    return line_keys.split(), line_values.split()


# ('house river tree car', 'дом река дерево машина')
d = get_list(input(), input())
print(*sorted(d.items()))


# var2
def decorator(func):
    def wrapper(*args, **kwargs):
        # распаковать args в две переменные
        keys, value = func(*args, **kwargs)
        # объединить две переменные в один словарь
        d = dict(zip(keys, value))
        return d  # тут нужно вместо print возвращать return,
        # чтобы не возвращалось None

    return wrapper


@decorator
def string(lst1, lst2):                   # тут я думаю всё понятно
    l1 = lst1.split()
    l2 = lst2.split()
    return l1, l2


# lst1 = 'house river tree car'
# lst2 = 'дом река дерево машина'
lst1 = input()
lst2 = input()

# вот тут функцию sorted нужно вызвать
print(*sorted(string(lst1, lst2).items()))
