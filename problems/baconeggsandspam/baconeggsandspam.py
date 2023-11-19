from collections import defaultdict
n = int(input())

while n != 0:
    d = defaultdict(list)
    for i in range(n):
        s = input().split()
        name = s[0]
        s = s[1:]
        for j in s:
            d[j].append(name)
    
    l = list(d.items())
    l.sort()
    for k,v in l:
        v.sort()
        print(k, *v)
    print()

    n = int(input())
