def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(int(input())))


# 2

t = [0] * 1000


def f(n):
    if n <= 1:
        return n
    else:
        if t[n - 1] == 0:
            t[n - 1] = f(n - 1)
        if t[n - 2] == 0:
            t[n - 2] = f(n - 2)
        t[n] = t[n - 1] + t[n - 2]
        return t[n]


print(f(int(input())))


# 3

#  Фибоначчи рекурсией с кэшем


def fib(n):
    if n in MEMO:
        return MEMO[n]
    MEMO[n] = fib(n - 1) + fib(n - 2)
    return MEMO[n]


n = int(input())
MEMO = {0: 0, 1: 1}

print(fib(n))

