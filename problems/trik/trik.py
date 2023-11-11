l = [1, 2, 3]
s = input()

for c in s:
    if c == 'A':
        l[0], l[1] = l[1], l[0]
    elif c == 'B':
        l[1], l[2] = l[2], l[1]
    elif c == 'C':
        l[0], l[2] = l[2], l[0]

print(l.index(1) + 1)