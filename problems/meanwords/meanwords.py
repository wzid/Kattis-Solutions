n = int(input())

l = []
for i in range(n):
    s = input()
    for i, c in enumerate(s):
        if i >= len(l):
            l.append((ord(c), 1))
        else:
            l[i] = (l[i][0] + ord(c), l[i][1] + 1)

res = ''
for i in range(len(l)):
    res += chr(l[i][0] // l[i][1])
print(res)