import sys
n = int(input())

last = input()
should = True
absent = []
for line in sys.stdin:
    line = line.rstrip()
    if should:
        if line == 'Present!':
            should = False
        else:
            absent.append(last)
            last = line
    else:
        should = True
        last = line
    
if should:
    absent.append(last)


if absent:
    for v in absent:
        print(v)
else:
    print('No Absences')