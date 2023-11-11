l = []
for i in range(5):
    s = input()
    if 'FBI' in s:
        l.append(i+1)

if not l:
    print('HE GOT AWAY!')
else:
    print(*l)
    