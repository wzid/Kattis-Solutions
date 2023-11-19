n = int(input())
l = list(map(int, input().split()))
res = []
last = 0
for v in l:
    if v >= last:
        res.append(v)
        last = v
print(len(res))
print(*res)