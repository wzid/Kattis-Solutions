import sys

d = {};space = False
for line in sys.stdin:
    line = line.strip()
    if line.strip() == '':
        space = True
        continue
    if not space:
        m = line.split()
        d[m[1]] = m[0]
    else:
        if line in d:
            print(d[line])
        else:
            print('eh')
