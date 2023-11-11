import math

b, B = map(int, input().split())
nine = 90 * (3.14159265358979323846 / 180)
bdfbd = B * (3.14159265358979323846 / 180)
print(math.ceil((b * math.sin(nine)) / math.sin(bdfbd)))