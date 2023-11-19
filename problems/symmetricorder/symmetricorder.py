n = int(input())
ind = 1
while n != 0:
    l = []
    for i in range(n):
        l.append(input())
    l.sort(key=lambda x: len(x))
    new_l = [''] * n
    s, e = 0, n-1
    m = True
    print(f'SET {ind}')
    for i in range(n):
        if m:
            new_l[s] = l[i]
            m = False
            s += 1
        else:
            new_l[e] = l[i]
            m = True
            e -= 1
    for i in range(n):
        print(new_l[i])

    n = int(input())
    ind += 1
