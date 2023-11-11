n = input()
s = ''
last = ''
for c in n:
    if c != last:
        s += c
    last = c
print(s)