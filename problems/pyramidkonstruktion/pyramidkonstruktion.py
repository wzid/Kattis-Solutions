h, n, m = map(int, input().split())

# sum formula
# number of 2x2 blocks
needed = 1 + (4 * ((h * (h - 1)) // 2)) 
needed -= n + (m * 2)

if needed < 0:
    # we need the top
    if n == 0:
        print(1, 0)
    else:
        print(0, 0)
else:
    print(needed % 2, needed // 2)