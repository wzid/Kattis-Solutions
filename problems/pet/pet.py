s = 0
ind = -1
for i in range(5):
    a = sum(list(map(int, input().split())))
    if s < a:
        s = a
        ind = i

print(ind+1, s)