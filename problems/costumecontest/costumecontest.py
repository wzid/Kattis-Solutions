from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in range(n):
    s = input()
    d[s] += 1

l = [(v, k) for k, v in d.items()]
l.sort()
x = l[0][0]
also = [l[0][1]]
ind = 1
while True:
    if ind >= len(l):
        break
    if l[ind][0] == x:
        also.append(l[ind][1])
        ind += 1
    else:
        break

also.sort()
for i in also:
    print(i)