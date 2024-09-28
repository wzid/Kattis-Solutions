n = int(input())
rows = []
for i in range(n):
    rows.append([int(x) for x in input().split()])

result = []
for row in rows:
    val = 0
    for v in row:
        val |= v
    result.append(val)
print(*result)