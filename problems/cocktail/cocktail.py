n, t = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))

l.sort(reverse=True)
new = []
for i in range(n):
    for j in range(len(new)):
        new[j] -= t
    if 0 in new:
        print('NO')
        exit()
    new.append(l.pop(0))
print('YES')