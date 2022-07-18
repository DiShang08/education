file = open('numbers.txt', 'r', encoding='utf-8')
summa = 0
count = 0
for line in file:
    if len(line.strip()) == 3:
        count += 1
    elif len(line.strip()) == 2:
        summa += int(line.strip())
print(count, summa)
