ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))

n, c, p = mii()
t = 0
for i in range(n):
    x = ii()
    if x > c + p:
        p = c
        c = x
        t += 1
print(t)

