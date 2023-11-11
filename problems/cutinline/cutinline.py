n = int(input())

l = []
for i in range(n):
    l.append(input())

instructions = int(input())

for i in range(instructions):
    inp = input().split()
    if inp[0] == 'cut':
        a, b = inp[1], inp[2]
        ind = l.index(b)
        l.insert(ind, a)
    elif inp[0] == 'leave':
        a = inp[1]
        l.remove(a)

for c in l:
    print(c)
        