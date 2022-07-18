# ki, kj = map(int, input().split())
# b = [['.']*12 for i in range(12)]
# moves = [[1, 2], [1, -2], [-1, 2], [-1, -2],
#          [2, 1], [2, -1], [-2, 1], [-2, -1]]
# kj += 1
# ki += 1
# for di, dj in moves:
#     i = ki + di
#     j = kj + dj
#     b[i][j] = '*'
# b[ki][kj] = 'N'
# for row in b[2:-2]:
#     print(' '.join(row[2:-2]))

# 1
s = [["." for i in range(15)] for j in range(15)]
for i in [5, 9]:
    for j in [6, 8]:
        s[i][j] = s[j][i] = '*'
s[7][7] = 'N'

st = input()
x = int(st[1])
y = ord(st[0]) - ord('a') + 1
for i in range(x-1, 7+x):
    for j in range(8-y, 16-y):
        print(s[i][j], end=' ')
    print()

# 2
x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
board[y][x] = 'N'

for i in range(n):
    for j in range(n):
        if abs(y - i) * abs(x - j) == 2:
            board[i][j] = '*'

for row in board:
    print(*row)
