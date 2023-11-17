cur = []
periods = []
for i in range(2):
    d, y = map(int, input().split())
    cur.append(d)
    periods.append(y)

res = 0
while res == 0 or cur != [0, 0]:
    res += 1
    cur = [(x + 1) % y for x, y in zip(cur, periods)]

print(res)
