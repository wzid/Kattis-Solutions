input()
l = list(map(int, input().split()))
l.sort(reverse=True)
a, b = 0, 0
g = True
for v in l:
    if g:
        a += v
    else:
        b += v
    g = not g
print(a, b)