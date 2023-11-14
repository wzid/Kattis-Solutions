n = int(input())


sum_min = 0
sum_sec = 0
for i in range(n):
    m, s = map(int, input().split())
    sum_min += m
    sum_sec += s

m = sum_sec / 60 / sum_min
if m > 1:
    print(m)
else:
    print("measurement error")