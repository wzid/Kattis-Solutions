n, s, m = map(int, input().split())

visited = set()
board = [int(x) for x in input().split()]

pos = s - 1

hops = 0
while True:
    num = board[pos]
    if pos in visited:
        print('cycle')
        print(hops)
        exit()
    visited.add(pos)
    if num == m:
        print('magic')
        print(hops)
        exit()
    if num < 0:
        if pos - abs(num) < 0:
            print('left')
            print(hops+1)
            exit()
        else:
            pos -= abs(num)
    else:
        # is this greater than or equal?
        if pos + num >= len(board):
            print('right')
            print(hops+1)
            exit()
        else:
            pos += num
    hops += 1
        