n = int(input())
for i in range(n):
    l = input()
    s = 'Simon says '
    if l.startswith(s):
        o = l[len(s):]
        print(o)
        