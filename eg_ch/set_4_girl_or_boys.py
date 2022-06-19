
# var_1

a = input()
s = set()
for i in a:
    if i not in s:
        s.add(i)
print("IGNORE HIM!" if len(s) % 2 != 0 else "CHAT WITH HER!")

# var_2

print(["CHAT WITH HER!", "IGNORE HIM!"][len({*input()}) % 2])

# var_3

print(['CHAT WITH HER!', 'IGNORE HIM!'][len(set(input())) % 2])
