i = 1
from sys import stdin
from collections import defaultdict
times = defaultdict(int)
enter_time = defaultdict(int)
canEnter = False
for line in stdin:
    line = line.strip()
    if line == 'OPEN':
        canEnter = True
    elif line == 'CLOSE':
        if i > 1:
            print()
        print(f'Day {i}')
        l = []
        for k, v in times.items():
            l.append((k, v))
        l.sort()
        for k, v in l:
            print(k, f'${v*.1:.2f}')
        i += 1
        times.clear()
        enter_time.clear()
    else:
        x, name, time = line.split()
        if x == 'ENTER':
            enter_time[name] = int(time)
        elif x == 'EXIT':
            times[name] += int(time) - enter_time[name]
        

