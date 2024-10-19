grid = [input() for _ in range(3)]

for i in range(3):
    if grid[i] == 'OOO':
        print('Jebb')
        quit()
    elif grid[i] == 'XXX':
        print('Neibb')
        quit()

for i in range(3):
    if grid[0][i] == 'X' and grid[1][i] == 'X' and grid[2][i] == 'X':
        print('Neibb')
        quit()
    elif grid[0][i] == 'O' and grid[1][i] == 'O' and grid[2][i] == 'O':
        print('Jebb')
        quit()

if grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X':
    print('Neibb')
    quit()

if grid[0][0] == 'O' and grid[1][1] == 'O' and grid[2][2] == 'O':
    print('Jebb')
    quit()

if grid[0][2] == 'X' and grid[1][1] == 'X' and grid[2][0] == 'X':
    print('Neibb')
    quit()

if grid[0][2] == 'O' and grid[1][1] == 'O' and grid[2][0] == 'O':
    print('Jebb')
    quit()

print('Neibb')

