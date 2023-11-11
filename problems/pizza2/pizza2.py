import math

r, c = [int(x) for x in input().split()]

if c >= r:
    print(0.0)
else:
    res = (math.pi * r**2)
    print( ((math.pi * (r-c)**2) / res) * 100.0)