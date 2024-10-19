n, m, k = map(int, input().split())
coords = set()
for i in range(k):
    y, x = map(int, input().split())
    coords.add((y-1, x-1))


for i in range(n):
    s = ''
    for j in range(m):
        if (i, j) in coords:
            s += '*'
        else:
            s += '.'
    print(s)