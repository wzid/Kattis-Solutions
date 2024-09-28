import math

# (n+1)(n+2)/2

m = 10**9+7

# 1 3 6 10 15 21
def triangle(n):
    return (n+1)*(n+2)//2 % m

x, y = map(int, input().split())

print(triangle(x-2)*triangle(y-2) % m)