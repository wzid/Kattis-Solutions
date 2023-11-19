n = int(input())
while n != 0:
    s = [input() for _ in range(n)]
    s.sort(key = lambda x: x[0:2])
    for x in s:
        print(x)
    print()
    n = int(input())