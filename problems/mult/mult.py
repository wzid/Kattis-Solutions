n = int(input())

m = -1
times = []
for i in range(n-1):
    if m == -1:
        m = int(input())
    else:
        x = int(input())
        if x % m == 0:
            times.append(x)
            m = -1

for v in times:
    print(v)