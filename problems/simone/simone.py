n, k = map(int, input().split())

d = {}

for i in range(1, k+1):
    d[i] = 0

s = list(map(int, input().split()))

for i in range(n):
    d[s[i]] += 1

l = [(v, k) for k, v in d.items()]
l.sort()

s = l[0][0]
n = [l[0][1]]
ind = 1
while True:
    if ind >= len(l):
        break
    if l[ind][0] == s:
        n.append(l[ind][1])
    else:
        break
    ind += 1
    
n.sort()
print(len(n))
print(*n)