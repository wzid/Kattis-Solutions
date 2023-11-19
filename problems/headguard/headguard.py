from sys import stdin

for line in stdin:
    line = line.rstrip()
    current = line[0]
    num = 0
    res = ''
    for c in line:
        if c == current:
            num += 1
        else:
            res += str(num) + current
            current = c
            num = 1
    print(res + str(num) + current)
