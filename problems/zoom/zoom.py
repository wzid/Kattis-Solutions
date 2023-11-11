n, k = map(int, input().split())

j = 1
l = list(map(int, input().split()))
result = []

for i, v in enumerate(l):
    if j == k:
        result.append(v)
        j = 1
    else:
        j += 1
print(*result)
    