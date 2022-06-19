# Есть два словаря, нужно их объединить в новый словарь rez и вывести его на экран

# var_1

d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
rez = d1.copy()
for key, value in d2.items():
    rez[key] = value
print(rez)

# var_2

d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
rez = dict(d1)
rez.update(d2)
print(rez)
