# var1
from functools import wraps


def sum_decor(start=0):
    def func_decor(func):
        def inner(string):
            return func(string) + start
        return inner
    return func_decor


@sum_decor(start=5)
def f(string):
    return sum(list(map(int, string.split())))


s = input()
print(f(s))


# var2


class Adding:
    # запоминаем аргументы декоратора
    def __init__(self, start=1):
        self._start = start

    # декоратор общего назначения
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            val += self._start
            return val
        return wrapper


@Adding(start=5)
def str_sum(s):
    return sum((int(_) for _ in s.split()))


s = input()
print(str_sum(s))
