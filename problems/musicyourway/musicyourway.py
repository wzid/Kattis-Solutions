attributes = input().split()
m = int(input())
l = [input().split() for _ in range(m)]
n = int(input())
for j in range(n):
    sort_by = input()
    ind = attributes.index(sort_by)
    l.sort(key=lambda x: x[ind])
    
    print(*attributes)
    for v in l:
        print(*v)
    if j != n-1:
        print()
