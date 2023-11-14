a, b = map(int, input().split())

c = a * b

l = []
for i in range(a, b+1):
    for j in range(i, a-1, -1):
        xy = i * j
        if sorted(str(i) + str(j)) == sorted(str(xy)):
            l.append((j, i))

l.sort()
print(len(l), 'digit-preserving pair(s)')
for k, v in l:
    print(f'x = {k}, y = {v}, xy = {k*v}')
