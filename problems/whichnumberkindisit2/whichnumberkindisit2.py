ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))

t = ii()
for i in range(t):
    x = ii()
    s = x**(1/2)
    r = ''
    if x % 2 != 0:
        r += 'O'
    if s == int(s):
        r += 'S'
    if r:
        print(r)
    else:
        print('EMPTY')