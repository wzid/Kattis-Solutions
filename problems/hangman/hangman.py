s = input()
k = input()

d = 10

while len(s) > 0 and d > 0:
    if k[0] in s:
        s = s.replace(k[0], '')
    else:
        d -= 1
    
    k = k[1:]


if d == 0:
    print('LOSE')
else:
    print('WIN')