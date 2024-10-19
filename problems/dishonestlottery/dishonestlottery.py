n = int(input())
from collections import defaultdict
count = defaultdict(int)
results = []
for i in range(10*n):
    l = list(map(int, input().split()))
    for v in l:
        count[v] += 1
        if count[v] == (2 * n)+1:
            results.append(v)

if results:
    print(*sorted(results))
else:
    print(-1)