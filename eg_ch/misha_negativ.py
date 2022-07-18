# Программа сперва считывает числа n и m (1 ≤ n, m ≤ 100) – высоту и ширину исходного
# изображения (в пикселях). Последующие n строк содержат описание исходного
# изображения. Каждая строка состоит из m символов «B» и «W».
# Символ «B» соответствует черному пикселю, а символ «W» – белому.
# Далее следует пустая строка, а после нее – описание выведенного Мишиной
# программой изображения в том же формате, что и исходное изображение.
#
# Необходимо вывести на экран число пикселей негатива,
# которые неправильно сформированы Мишиной программой.

# Variant_1

n, m = map(int, input().split())
a = [input() for i in range(n)]
input()
b = [input() for j in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            count += 1
print(count)

# Variant_2

n, m = map(int, input().split())
a = [input() for i in range(n)]
input()
b = [input() for i in range(n)]
print(sum([a[r][c] == b[r][c] for r in range(n) for c in range(m)]))

# Variant_3_подробный

n, m = map(int, input().split())
start = []
finish = []
for i in range(n):
    start.append(input())
input()
for i in range(n):
    finish.append(input())
count = 0
for row in range(n):
    for col in range(m):
        if start[row][col] == finish[row][col]:
            count += 1
print(count)
