import math

n = int(input())
grav = 9.81
for i in range(n):
  v0, theta, x1, h1, h2 = map(float, input().split())


  t = x1 / v0 / math.cos(math.radians(theta))
  y1 = v0 * t * math.sin(math.radians(theta)) - 0.5 * grav * (t ** 2)

  if y1 > h1 + 1 and y1 < h2 - 1:
    print("Safe")
  else:
    print("Not Safe")