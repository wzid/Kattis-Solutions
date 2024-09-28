board = []

queens = set()
for i in range(8):
    x = input()
    for j in range(8):
        if x[j] == '*':
            queens.add((i,j))
    board.append(x)

if len(queens) != 8:
    print("invalid")
    exit()

for queen in queens:
    y, x = queen
    # check above:
    for i in range(y-1, -1, -1):
        if board[i][x] == '*':
            print("invalid")
            exit()
    
    # check below:
    for i in range(y+1, 8):
        if board[i][x] == '*':
            print("invalid")
            exit()
    # check left:
    if '*' in board[y][:x]:
        print("invalid")
        exit()
    # check right:
    if '*' in board[y][x+1:]:
        print("invalid")
        exit()
    
    # check upper left:
    yy, xx = y-1, x-1
    while yy >= 0 and xx >= 0:
        if board[yy][xx] == '*':
            print("invalid")
            exit()
        yy -= 1
        xx -= 1
    # check upper right:
    yy, xx = y-1, x+1
    while yy >= 0 and xx < 8:
        if board[yy][xx] == '*':
            print("invalid")
            exit()
        yy -= 1
        xx += 1
    # check lower left:
    yy, xx = y+1, x-1
    while yy < 8 and xx >= 0:
        if board[yy][xx] == '*':
            print("invalid")
            exit()
        yy += 1
        xx -= 1
    # check lower right:
    yy, xx = y+1, x+1
    while yy < 8 and xx < 8:
        if board[yy][xx] == '*':
            print("invalid")
            exit()
        yy += 1
        xx += 1
print('valid')