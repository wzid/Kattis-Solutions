l, r = 1, 1000

while l <= r:
    mid = (l + r) // 2

    print(mid)
    x = input()
    if x == 'correct':
        exit()
    elif x == 'lower':
        r = mid - 1
    elif x == 'higher':
        l = mid + 1