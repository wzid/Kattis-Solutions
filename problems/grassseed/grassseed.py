cost = float(input())
lawns = int(input())

s = 0.0
for i in range(lawns):
    w, l = map(float, input().split())
    s += cost * w * l
print(s)
    