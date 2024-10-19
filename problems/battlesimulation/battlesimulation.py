x = input()

s = []
skip_until = -1
check = ['B', "L", 'R']
last = ['','','']
for i, c in enumerate(x):
    if i < skip_until:
        continue
    
    if c == 'R':
        s .append('S')
    elif c == 'B':
        s.append('K')
    elif c == 'L':
        s.append('H')

    last[i % 3] = c
    if sorted(last) == check:
        s.pop()
        s.pop()
        s.pop()
        s.append('C')
        last = ['','','']

print(''.join(s))