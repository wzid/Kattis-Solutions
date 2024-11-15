r, c = map(int, input().split())
snake_org = [-1 for _ in range(16)]
grid = []

for y in range(r):
    row = input()
    to_add = []
    for x in range(c):
        to_add.append(row[x])
        if row[x].isdigit():
            snake_org[int(row[x])] = (x, y)
        elif row[x] in 'abcdef':
            snake_org[int(row[x], 16)] = (x, y)
    grid.append(to_add)

# shorten the array
snake_real_len = 0
while snake_real_len < 16 and snake_org[snake_real_len] != -1:
    snake_real_len += 1
snake = snake_org[:snake_real_len]

# last = hex(len(snake) - 1)[2:]
snake_body = ''
for i in range(1, len(snake)-1):
    snake_body += hex(i)[2:]


def slither(x_head_off, y_head_off, _snake):
    new_head_x, new_head_y = _snake[0][0] + x_head_off, _snake[0][1] + y_head_off
    
    if new_head_x >= c or new_head_y >= r or new_head_y < 0 or new_head_x < 0 or grid[new_head_y][new_head_x] in snake_body:
        return False
    
    tail_x, tail_y = _snake[-1]
    grid[tail_y][tail_x] = '.'
    
    for i in range(len(_snake)-1, 0, -1):
        next_x, next_y = _snake[i] = _snake[i-1]
        grid[next_y][next_x] = hex(i)[2:]

    if grid[_snake[0][1] + y_head_off][_snake[0][0] + x_head_off] in snake_body:
        return False
    
    _snake[0] = (_snake[0][0] + x_head_off, _snake[0][1] + y_head_off)
    
    grid[_snake[0][1]][_snake[0][0]] = '0'
    
    return True

offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def reset_grid(new_snake):
    for y in range(r):
        for x in range(c):
            if grid[y][x] != 'A':
                grid[y][x] = '.'
    
    for i, (x, y) in enumerate(new_snake):
        grid[y][x] = hex(i)[2:]

visited = set()
# print(f'{snake_body=}')
def search(x_head_off, y_head_off, _snake):
    new_head_x, new_head_y = _snake[0][0] + x_head_off, _snake[0][1] + y_head_off
    
    if new_head_x >= c or new_head_y >= r or new_head_y < 0 or new_head_x < 0 or grid[new_head_y][new_head_x] in snake_body or grid[new_head_y][new_head_x] == '1':
        return False
    
    if (new_head_x, new_head_y) in visited:
        return False
    
    # for v in grid:
    #     print(*v)
    # print()

    # at target!
    if grid[new_head_y][new_head_x] == 'A':
        print(1)
        exit()

    if not slither(x_head_off, y_head_off, _snake):
        return False

    if grid[new_head_y][new_head_x] in snake_body:
        # print(new_head_x, new_head_y)
        return False
    
    visited.add((new_head_x, new_head_y))

    

    for px, py in offsets:
        search(px, py, _snake.copy())
        reset_grid(_snake)
    
    visited.remove((new_head_x, new_head_y))

for px, py in offsets:   
    search(px, py, snake.copy())
    reset_grid(snake)

print(0)