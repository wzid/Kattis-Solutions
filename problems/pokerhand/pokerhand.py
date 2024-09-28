from collections import defaultdict
x = input().split()

d = defaultdict(int)

for v in x:
    d[v[0]] += 1

m = 0
for key, v in d.items():
    m = max(m, v)
print(m)
