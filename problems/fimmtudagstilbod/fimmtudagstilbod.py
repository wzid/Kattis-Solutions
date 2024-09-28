# n, x = map(int, input().split())
x = input()
if int(x) >= 2020:
    print(1000 + (100 * (int(x) - 2020)))
else:
    print(1000)