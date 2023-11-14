p = int(input())

for i in range(p):
    a, b = map(int, input().split())
    print(a, ((b * (b+1)) // 2) + b)
