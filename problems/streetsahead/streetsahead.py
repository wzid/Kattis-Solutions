n, q = (int(s) for s in input().split(' '))

names = {}
for i in range(n):
    names[input()] = i


for i in range(q):
    q1, q2 = (s for s in input().split(' '))
    index1 = names[q1]
    index2 = names[q2]
    print (abs(index1-index2)-1)