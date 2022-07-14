# Функция должна создать файл с названием "range_<number>.txt" и наполнить его
# целыми числами от 1 до n включительно, причем каждое число записывается
# в отдельной строке

# 1
def create_file_with_numbers(n):
    file = open(f'range_{n}.txt', 'w')
    for i in range(1, n+1):
        file.write(str(i)+'\n')
    file.close()


res = create_file_with_numbers(5)
print(res)


# 2
def create_file_with_numbers(n):
    with open(f'range_{n}.txt', mode='w', encoding='utf-8') as fw:
        fw.write('\n'.join(map(str, range(1, n + 1))))


# 3
# Версия №2. Используем функцию print с параметром file
def create_file_with_numbers(n):
    with open(f'range_{n}.txt', mode='w', encoding='utf-8') as fw:
        print(*range(1, n + 1), file=fw, sep='\n')
