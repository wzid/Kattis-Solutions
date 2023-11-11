adrian = 'ABC'
bruno = 'BABC'
goran = 'CCAABB'

a,b,g = 0,0,0

n = int(input())
s = input()

for i, c in enumerate(s):
    ind = i +1
    if c == adrian[i % len(adrian)]:
        a += 1
    if c == bruno[i % len(bruno)]:
        b += 1
    if c == goran[i % len(goran)]:
        g += 1

l = [(a, 'Adrian'), (b, 'Bruno'), (g, 'Goran')]
l.sort(reverse=True)
if l[0][0] == l[1][0] and l[1][0] == l[2][0]:
    print(l[0][0])
    print('Adrian')
    print('Bruno')
    print('Goran')
elif l[0][0] == l[1][0]:
    print(l[0][0])
    first, second = l[0][1], l[1][1]
    if first[0] < second[0]:
        print(first)
        print(second)
    else:
        print(second)
        print(first)
else:
    print(l[0][0])
    print(l[0][1])
