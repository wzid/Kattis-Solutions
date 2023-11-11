s = input()

looking = False
last = -1
for i, c in enumerate(s):
    if c == ':' or c == ';':
        looking = True
        last = i
    elif looking:
        if c == '-':
            continue
        elif c == ')':
            print(last)
            looking = False
        else:
            looking = False
