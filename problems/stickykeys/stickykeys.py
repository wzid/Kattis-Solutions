s = input()
last = ''
ss = ''
for c in s:
    if c != last:
        ss += c
    last = c
print(ss)