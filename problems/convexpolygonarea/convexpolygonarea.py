n = int(input())

def area(points):
    m = len(points)
    a = 0
    for i in range(m):
        next = (i + 1) % m
        x_1, y_1 = points[i]
        x_2, y_2 = points[next]
        a += x_1*y_2 - x_2*y_1
    return a/2


for i in range(n):
    m, *rest = map(int, input().split())
    points = list(zip(rest[::2], rest[1::2]))
    print(area(points))