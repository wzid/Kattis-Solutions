n = int(input())
s = set()
for i in range(n):
    l = input().split()
    if l[0] == 'entry':
        if l[1] in s:
            print(f'{l[1]} entered (ANOMALY)')
        else:
            print(f'{l[1]} entered')
            s.add(l[1])
    else:
        if l[1] in s:
            print(f'{l[1]} exited')
            s.remove(l[1])
        else:
            print(f'{l[1]} exited (ANOMALY)')