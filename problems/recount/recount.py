from collections import defaultdict
from sys import stdin

d = defaultdict(int)
for line in stdin:
    line = line.rstrip()
    if line == '***':
        break
    d[line] += 1


l = sorted(d.items(), key=lambda x: x[1], reverse=True)
if l[0][1] == l[1][1]:
    print('Runoff!')
else:
    print(l[0][0])