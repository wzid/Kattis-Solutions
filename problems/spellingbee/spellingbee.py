s = input()
n = int(input())

l = []
for i in range(n):
    x = input()
    if len(x) >= 4 and s[0] in x:
        found = True
        for c in x:
            if c not in s:
                found = False
        if found:
            l.append(x)
            

for vv in l:
    print(vv)