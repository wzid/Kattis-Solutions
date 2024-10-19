n, q = map(int, input().split())

from collections import defaultdict

initials = defaultdict(int)
initials_to_name = {}
for i in range(n):
    name = input().split()
    person_initials = name[0][0] + name[1][0] 
    initials[person_initials] += 1
    initials_to_name[person_initials] = ' '.join(name)

for i in range(q):
    yelled = input()
    if yelled in initials:
        if initials[yelled] == 1:
            print(initials_to_name[yelled])
        else:
            print('ambiguous')
    else:
        print('nobody')