input()

inp = input()
s = []

d = {']': '[', '}': '{', ')': '('}
for c in inp:
    if c in d:
        if s and s[-1] == d[c]:
            s.pop()
        else:
            print('Invalid')
            exit()
    else:
        s.append(c)
if not s:
    print('Valid')
else:
    print('Invalid')