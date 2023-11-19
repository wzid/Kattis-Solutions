def swap(l, a, b):
    l[a], l[b] = l[b], l[a]

l = list(map(int, input().split()))
sor = sorted(l)

while l != sor:
    if l[0] > l[1]:
        swap(l, 0, 1)
        print(*l)
    if l[1] > l[2]:
        swap(l, 1, 2)
        print(*l)
    if l[2] > l[3]:
        swap(l, 2, 3)
        print(*l)
    if l[3] > l[4]:
        swap(l, 3, 4)
        print(*l)