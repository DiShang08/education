def list_sort(func):

    def inner(s):
        return sorted(func(s))

    return inner


@list_sort
def get_list(s):
    return [int(i) for i in s.split()]


print(*get_list(input()))
