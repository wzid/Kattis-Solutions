from collections import deque
from math import ceil, log2

ii = lambda:int(input())
mii = lambda:map(int, input().split())
lmii = lambda:list(map(int, input().split()))

n, c = mii()
pillows = []

lowest = float('inf')
for i in input().split():
    pillows.append(int(i))
    if pillows[-1] < lowest:
        lowest = pillows[-1]

dp = set([0])

for i in range(0,int(log2(lowest))):
    nxt = set()
    for x in dp:
        for j in range(len(pillows)):
            thing = x + ceil(pillows[j] / (2**i))
            if thing <= c:
                nxt.add(thing)
    if c in nxt:
        print("YES")
        exit(0)
    dp = nxt
    if len(nxt) == 0:
        print("NO")
        exit(0)

if len(dp):
    print("YES")