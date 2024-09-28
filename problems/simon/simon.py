import sys

n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline()
    if 'simon says' in line:
        sys.stdout.write(' '.join(line.split('simon says ')[1:]) + '\n')
    else:
        sys.stdout.write('\n')
        