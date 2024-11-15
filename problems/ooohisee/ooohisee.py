ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))

r, c = mii()
grid = []
for i in range(r):
    grid.append([c for c in input()])

res = []

offsets = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
for y in range(r):
    for x in range(c):
        if grid[y][x] != '0':
            continue

        if y+1 >= r or x+1 >= c or x-1 < 0 or y-1 < 0:
            continue

        works = True
        for px, py in offsets:
            if grid[y+py][x+px] != 'O':
                works = False
                break
        if works:
            res.append((x+1, y+1))

if res:
    if len(res) > 1:
        print(f'Oh no! {len(res)} locations')
    else:
        print(*res[0][::-1])
else:
    print('Oh no!')