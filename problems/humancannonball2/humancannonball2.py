import math
n = int(input())

for i in range(n):
    v_0, theta, x_1, h1, h2 = map(float, input().split())

    #check
    t = (x_1/ v_0) / math.cos(math.radians(theta))

    y = v_0*t*math.sin(math.radians(theta)) - ((9.81*t**2)/2)

    if h2 - y > 1 and y - h1 > 1:
        print('Safe')
    else:
        print('Not Safe')