from sys import stdin
for line in stdin:
    line = line.strip()
    a, b = map(int, line.split())
    print(abs(a-b))