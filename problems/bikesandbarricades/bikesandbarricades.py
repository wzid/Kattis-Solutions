n = int(input())

m = float('inf')
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    if (x2 - x1) == 0:
        slope = 0
    else:
        slope = (y2 - y1) / (x2 - x1)
    b = y1 - (slope * x1)
    if (x1 > 0 and x2 > 0) or (x2 < 0 and x1 < 0):
        pass
    elif b > 0:
        m = min(m, b)

if m == float('inf'):
    print(-1.0)
else:
    print(m)