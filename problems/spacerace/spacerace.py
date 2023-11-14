n = int(input())
d = float(input())
winner = ''
eff = 0
for i in range(n):
    j = input().split()
    name = j[0]
    v = float(j[1])
    r = float(j[2])
    t = d / v
    rate = r / t
    e = v / rate
    if e > eff:
        eff = e
        winner = name
print(winner)