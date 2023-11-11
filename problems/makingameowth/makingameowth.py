n, p, x, y = map(int, input().split())
if n > p:
    print(p*x)
else:
    print(str((int(p / (n - 1)) * y) + (p * x)))