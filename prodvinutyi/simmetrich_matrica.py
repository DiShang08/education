n = int(input())
s = [input().split() for _ in range(n)]
s1 = [[s[j][i] for j in range(n)] for i in range(n)]

print(s, s1, sep='\n')
print('YES' if s == s1 else 'NO')
