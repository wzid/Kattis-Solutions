t = int(input())

ship = []
for i in range(t):
    m = {}
    n = int(input())
    for j in range(n):
        s = input().split()
        if s[0] in m:
            m[s[0]] += int(s[1])
        else:
            m[s[0]] = int(s[1])
    ship.append(m)

for item in ship:
    print(len(item))
    a = sorted(item.items(), key=lambda x: (-x[1], x[0]))
    for i in a:
        print(i[0], i[1])