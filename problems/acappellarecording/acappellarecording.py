n, d = map(int, input().split())

l = [int(input()) for _ in range(n)]

l.sort()

last = l[0]
subsets = 1
for i in range(1, len(l)):
    if l[i] - last > d:
        subsets += 1
        last = l[i]
        
print(subsets)