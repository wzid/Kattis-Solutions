translation = {}
while (x := input()) != '':
    a, b = x.split()
    translation[b] = a

import sys

for line in sys.stdin:
    line = line.strip()
    if line in translation:
        print(translation[line])
    else:
        print('eh')
