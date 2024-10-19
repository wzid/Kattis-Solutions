n, r, c = map(int, input().split())

rows = []
for i in range(r):
    l = input().split()
    rows.append(l[0])
ind = 0
for i in range(0, n):
    x = input()
    if i % c != 0:
        continue
    if rows[ind] == x:
        print('left')
    else:
        print('right')

    ind += 1