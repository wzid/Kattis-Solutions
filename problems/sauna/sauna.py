

ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))

n = ii()
nums = []
a = -1
b = 999_999_999
for _ in range(n):
    aa, bb = mii()
    a = max(a, aa)
    b = min(b, bb)

if b < a:
    print('bad news')
else:
    print(b-a+1, a)