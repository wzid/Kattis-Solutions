h, k, v, s = map(int, input().split())
ss = 0
while h > 0:
    v += s
    v -= max(1, v // 10)
    if v >= k:
        h += 1
    if 0 < v and v < k:
        h -= 1
        if h == 0:
            v = 0
    if v <= 0:
        h = v = 0
    if s > 0:
        s-= 1
    ss += v

print(ss)