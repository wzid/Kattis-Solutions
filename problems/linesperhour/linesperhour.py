n, lph = map(int, input().split())

l = []

for i in range(n):
    l.append(int(input()))
l.sort()

rate = 5 * lph
total = 0
i = 0
for v in l:
    if total + v <= rate:
        total += v
        i += 1
    else:
        break
print(i)