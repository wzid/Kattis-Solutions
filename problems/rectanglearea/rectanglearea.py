import math
x1, y1, x2, y2 = map(float, input().split())

def distance(xy1: list, xy2: list) -> float:
    return math.sqrt((xy2[1] - xy1[1])**2 + (xy2[0] - xy1[0])**2)
    
width = abs(x1 - x2)
height = abs(y1 - y2)
print(width*height)