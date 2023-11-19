import sys
i = 1
for line in sys.stdin:
    line = line.rstrip()
    line = list(map(int, line.split()))[1:]
    mi = min(line)
    ma = max(line)
    print(f'Case {i}:', mi, ma, ma - mi)
    i+=1