n = int(input())


last = ''
other = []
for i in range(n):
    s = input()
    if last != '' and s != 'Present!' and last != 'Present!':
        other.append(last)
    last = s
if last != 'Present!':
    other.append(last)

if other:
    for v in other:
        print(v)
else:
    print('No Absences')
        