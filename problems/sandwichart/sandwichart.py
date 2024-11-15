ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))

n, g, d, m = mii()
cur = mii()
genres = []

for i in range(g):
    l = mii()
    genres.append(set(l))
from collections import defaultdict
require = defaultdict(set)

for i in range(d):
    a, b = mii()
    require[a].add(b)

# apply requirements
curPtr = 0
curSet = set(cur)
while curPtr < len(cur):
    dep = cur[curPtr]
    if require[dep]:
        for need in require[dep]:
            if need not in curSet:
                cur += [need]
                curSet.add(need)
    curPtr += 1

# check if too many ingredients
if len(cur) > m:
    print('disaster')
    quit()

# check genres if this sandwhich qualifies as masterpiece
for genre in genres:
    if curSet.issubset(genre):
        print('masterpiece')
        quit()

print('disaster')