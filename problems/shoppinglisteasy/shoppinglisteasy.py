n, m = map(int,input().split())

l = set(input().split())
for i in range(n-1):
    l2 = set(input().split())
    l = l.intersection(l2)
print(len(l))
l = sorted(l)
for v in l:
    print(v)