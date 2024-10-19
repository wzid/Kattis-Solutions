n = int(input())

grid = []
for _ in range(n):
    grid.append([c for c in input()])

def fill(x_dir, y_dir, x, y):
    x += x_dir
    y += y_dir
    while x >= 0 and y >= 0 and x < n and y < n:
        if grid[y][x] == '?':
            print(0)
            exit()
        if grid[y][x] != '.' and grid[y][x] != '#':
            break
        grid[y][x] = '#'
        x += x_dir
        y += y_dir


dirs = [(0,1),(1,0),(0,-1),(-1,0)]
for y in range(n):
    for x in range(n):
        curr_val = grid[y][x]
        if curr_val == '?':
            for x_dir, y_dir in dirs:
                fill(x_dir, y_dir, x, y)
        elif curr_val.isdigit():
            count = 0
            for x_dir, y_dir in dirs:
                x2, y2 = x + x_dir, y + y_dir
                if x2 >= 0 and y2 >= 0 and x2 < n and y2 < n:
                    count += grid[y2][x2] == '?'
            if count != int(curr_val):
                print(0)
                exit()

for y in range(n):
    for x in range(n):
        if grid[y][x] == '.':
            print(0)
            exit()

print(1)