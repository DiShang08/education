# Ваша задача написать функцию format_namelist, которая принимает список словарей,
# у каждого словаря в списке есть только ключ name
#
# Функция format_namelist должна вернуть отформатированную строку, в которой все имена
# из списка разделяются запятой кроме последних двух имен, они должны быть разделены
# союзом "и". Если в списке нет ни одного имени, функция должна вернуть пустую строку.

# 1

def format_namelist(s):
    d = []
    c = ''
    for i in s:
        d.append(*i.values())
    if len(d) == 0:
        return ''
    elif len(d) == 1:
        return d[0]
    else:
        c = ', '.join(d[:-1])
        c = c + ' и ' + d[-1]
        return c


# s = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]
# print(format_namelist(s))

# 2

def format_namelist(lst):
    lst = [i['name'] for i in lst]
    string = ', '.join(lst[:-2] + [f'{lst[-2]} и {lst[-1]}']) if len(lst) >= 2 else ''.join(lst)
    return string
