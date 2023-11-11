from collections import defaultdict

s = input()

d = defaultdict(int)

for c in s:
    d[c] += 1

points = 0
tablet = 0
compass = 0
gear = 0
for k, v in sorted(d.items()):
    if k == 'T':
        tablet += v
    elif k == 'C':
        compass += v
    else:
        gear += v

points += min(tablet, compass, gear) * 7
points += tablet**2 + compass**2 + gear**2
print(points)