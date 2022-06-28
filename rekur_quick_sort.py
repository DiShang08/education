# функция quick_sort должна выполнить сортировку
def quick_sort(s):
    if len(s) <= 1:
        return s

    elem = s[0]
    # left = list(filter(lambda x: x < elem, s))
    # center = [i for i in s if i == elem]
    # right = list(filter(lambda x: x > elem, s))

    left = [i for i in s if i < elem]
    center = [i for i in s if i == elem]
    right = [i for i in s if i > elem]

    return quick_sort(left) + center + quick_sort(right)


print(*quick_sort([19, 4, 5, 17, 1]))
