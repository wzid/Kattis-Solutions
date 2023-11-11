s = input().split(';')

ssum = 0
for v in s:
    if '-' in v:
        first, second = map(int, v.split('-'))
        ssum += (second - first) + 1
    else:
        ssum += 1

print(ssum)