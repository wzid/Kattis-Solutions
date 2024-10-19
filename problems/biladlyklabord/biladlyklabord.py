last = ''
s = ''
for c in input():
    if c != last:
        s += c
    last = c
print(s)