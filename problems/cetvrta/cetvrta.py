
d = {}
h = {}
for i in range(3):
    a, b = map(int, input().split())
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
        
    if b not in h:
        h[b] = 1
    else:
        h[b] += 1

gg = 0
for k, v in d.items():
    if v == 1:
        gg = k
        break
hh2 = 0
for k, v in h.items():
    if v == 1:
        hh2 = k
        break
print(gg, hh2)