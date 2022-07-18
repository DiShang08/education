def chunked(a, n):
    s = []
    for i in range(0, len(a), n):
        s.append(a[i:i+n])
    return s


a = input().split()
n = int(input())
print(chunked(a, n))
