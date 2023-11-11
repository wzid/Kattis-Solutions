n = int(input())

l = []
for i in range(n):
    x, y = map(int, input().split())
    r = range(x, y+1)
    l.extend(r)
print(len(set(l)))