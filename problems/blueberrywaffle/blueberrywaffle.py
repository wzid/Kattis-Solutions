r, f = map(int, input().split())

if int((f + r/2) / r) % 2 == 0:
    print('up')
else:
    print('down')