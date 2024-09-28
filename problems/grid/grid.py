def bfs(grid, source, target):
    from collections import deque
    visited = {}
    queue = deque()
    found = 0

    visited[source] = True
    queue.append(source)

    while len(queue) > 0:
        m = queue.popleft()
        startX, startY = m[0], m[1]

        k = int(grid[startY][startX])

        directions = [(0, k), (k, 0), (0, -k), (-k, 0)]
        for deltaX, deltaY in directions:
            x, y = startX + deltaX, startY + deltaY

            if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
                continue

            if (x, y) not in visited:
                visited[(x, y)] = 1 + visited[(startX, startY)]
                queue.append((x, y))
                if (x, y) == target:
                    found = visited[(startX, startY)] + 1
                    break

        if found:
            return found

    return False


h, w = map(int, input().split())
grid = []

for i in range(h):
    grid.append(input())

result = bfs(grid, (0,0), (w-1, h-1))
if not result:
    print(-1)
else:
    print(result-1)