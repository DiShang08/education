n = int(input())
ch1, ch2, ch3, ch4 = 0, 0, 0, 0
for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        ch1 += 1
    elif x < 0 and y > 0:
        ch2 += 1
    elif x < 0 and y < 0:
        ch3 += 1
    elif x > 0 and y < 0:
        ch4 += 1
print(
    "Первая четверть: " + str(ch1), "Вторая четверть: " + str(ch2), "Третья четверть: " + str(ch3), "Четвертая четверть: " + str(ch4), sep='\n')

print(f'Первая четверть: {ch1}', f'Вторая четверть: {ch2}',
      f'Третья четверть: {ch3}', f'Четвертая четверть: {ch4}', sep='\n')
