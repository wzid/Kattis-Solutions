n = int(input())

combos = {}
for i in range(n):
    l = tuple(sorted([*map(int, input().split())]))
    if l in combos:
        combos[l] += 1
    else:
        combos[l] = 1

m = max(combos.values())
s = 0
for v in list(combos.values()):
    if v == m:
        s += m 
print(s)
