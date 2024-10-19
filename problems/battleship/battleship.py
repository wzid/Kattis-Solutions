t = int(input())

for _ in range(t):
    w, h, n = map(int, input().split())

    p1_grid = []
    p1_ships = 0
    for _ in range(h):
        p1_grid.append([c for c in input()])
        p1_ships += p1_grid[-1].count('#')
    
    p2_grid = []
    p2_ships = 0
    for _ in range(h):
        p2_grid.append([c for c in input()])
        p2_ships += p2_grid[-1].count('#')
        
    
    turn = True
    for _ in range(n):
        x, y = map(int, input().split())
        y = h - y - 1
        if (p2_ships == 0 or p1_ships == 0) and turn:
            continue
        if 0 <= x < w and 0 <= y < h:
            if turn:
                if p2_grid[y][x] == '#':
                    p2_grid[y][x] = '_'
                    p2_ships -= 1
                    if p2_ships == 0:
                        turn = not turn
                else:
                    turn = not turn
            else:
                if p1_grid[y][x] == '#':
                    p1_grid[y][x] = '_'
                    p1_ships -= 1
                    if p1_ships == 0:
                        turn = not turn
                else:
                    turn = not turn
        else:
            print("Invalid coordinates")

    if (p2_ships == 0 and p1_ships == 0) or (p2_ships > 0 and p1_ships > 0):
        print('draw')
    elif p1_ships == 0:
        print('player two wins')
    else:
        print('player one wins')