from collections import defaultdict

p, e = input().split()

d = defaultdict(int)

for c in p:
    d[c] += 1

ind = 0
for c in e:
    if ind == len(p):
        print('PASS')
        exit()
    elif p[ind] == c:
        d[c] -= 1
        if d[c] == 0:
            del d[c]
        ind += 1
    elif c in d:
        print('FAIL')
        exit()

if ind < len(p):
    print('FAIL')
else:
    print('PASS')
