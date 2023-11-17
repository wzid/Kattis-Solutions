n = int(input())
k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []
for i in range(n):
    l = [k[i], a[i], b[i]]
    l.remove(min(l))
    l.remove(max(l))
    res.append(l[0])
print(*res)