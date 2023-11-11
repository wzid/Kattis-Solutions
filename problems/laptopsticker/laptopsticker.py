wc, hc, ws, hs = map(int, input().split())

if ws <= wc - 2 and hs <= hc - 2:
    print(1)
else:
    print(0)