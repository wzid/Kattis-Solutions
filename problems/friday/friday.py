t = int(input())

if t == 0:
    print(0)

for _ in range(t):
    d, m = [int(x) for x in input().split()]
    month_days = [int(x) for x in input().split()]

    i = 1
    s = 0
    for days in month_days:
        if days >= 13 and ((i + 12) % 7) == 6:
            s += 1
        i += days
    print(s)