from collections import defaultdict
n = int(input())
ind = 1
while n != 0:
    d = defaultdict(int)
    for i in range(n):
        s = input().split()
        type = s[-1]
        
        d[type.lower()] += 1
    
    print(f'List {ind}:')
    l = list(d.items())
    l.sort(key=lambda x: x[0])
    for k,v in l:
        print(f'{k} | {v}')
    n = int(input())
    ind += 1