n, m = map(int, input().split())
l = list(map(int, input().split()))

not_ac = 0
for i, v in enumerate(l):
    if n < v:
        not_ac += 1  
        continue
    n -= v

print(not_ac)