def print_goods(*args):
    count = 1
    for i in args:
        if isinstance(i, str) and i.isalnum():
            print(f'{count}. {i}')
            count += 1
    if count == 1:
        print("Нет товаров")


print_goods('apple', 'banana', 'orange')
print_goods(1, True, 'Грушечка', '', 'Pineapple')
print_goods([], {}, 1, 2)


# def info_kwargs(**kwargs):
#     for k, v in sorted(kwargs.items()):
#         print(k, '=', v)
#         print(f'{k} = {v}')
#
#
# info_kwargs(first_name="John", last_name="Doe", age=33)
