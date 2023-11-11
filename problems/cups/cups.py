n = int(input())

l = []
for i in range(n):
    a, b = input().split()
    if a.isnumeric():
        a = int(a) // 2
        l.append((a, b))
    else:
        b = int(b)
        l.append((b, a))

l.sort(key=lambda x: x[0])
l = [x[1] for x in l]
for i in l:
    print(i)