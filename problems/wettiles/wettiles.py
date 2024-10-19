from collections import deque
    


# 2 2 6 6 
# 6 2 1 7
# 8 2 8 2

dirs = [(0,1),(0,-1),(1,0),(-1,0)]

while (first := input()) != '-1':
    width, height, t, l, w = map(int, first.split())
    
    def adjust_y(y):
        return height - y - 1
    # 2 = leak
    # 1 = wet tile
    # 0 = non wet tile
    # 3 = wall
    grid = [[0 for _ in range(width)] for _ in range(height)]

    queue = deque()
    leak_count = 0
    while leak_count != l:
        line = input().split()
        for i in range(0, len(line), 2):
            leak_count += 1
            x1, y1 = int(line[i])-1, int(line[i+1])-1
            y1 = adjust_y(y1)
            grid[y1][x1] = 2 # 2 is a leak
            queue.append((x1, y1, 1))
    
    wall_count = 0
    while wall_count != w:
        line = input().split()
        for i in range(0, len(line), 4):
            wall_count += 1
            x1, y1, x2, y2 = int(line[i])-1, int(line[i+1])-1, int(line[i+2])-1, int(line[i+3])-1
            y1 = adjust_y(y1)
            y2 = adjust_y(y2)

            if x1 != x2 and y1 == y2:
                for i in range(min(x1, x2), max(x1, x2)+1):
                    grid[y1][i] = 3
            elif x1 == x2 and y1 != y2:
                for i in range(min(y1, y2), max(y1, y2)+1):
                    grid[i][x1] = 3
            else:
                if x1 >= x2:
                    temp_y = y2
                    for j in range(x2, x1+1):
                        grid[temp_y][j] = 3
                        if y1 > y2:
                            temp_y += 1
                        else:
                            temp_y -= 1
                else:
                    temp_y = y1
                    for j in range(x1, x2+1):
                        grid[temp_y][j] = 3
                        if y1 > y2:
                            temp_y -= 1
                        else:
                            temp_y += 1
    # for i in range(height):
    #     print(*grid[i])


    def can_visit(x, y) -> bool:
        if x >= width or y >= height or y < 0 or x < 0:
            return False
        # if its wet or a wall we dont want to visit
        # dont want to add to queue a second time
        # or influence the wet tile count
        return grid[y][x] == 0

    # after walls lol
    total_wet = 0
    while queue:
        x1, y1, _t = queue.popleft()
        if _t > t:
            # if the thing in the queue would take more time then we have
            # since we are doing bfs i believe we can just exit
            break
        total_wet += 1
        for x_dir, y_dir in dirs:
            if not can_visit(x1+x_dir, y1+y_dir):
                continue
            if grid[y1+y_dir][x1+x_dir] == 1: 
                
                continue

            grid[y1+y_dir][x1+x_dir] = 1
            queue.append((x1+x_dir,y1+y_dir, _t + 1))
    
    # for i in range(height):
    #     print(*grid[i])
    print(total_wet)