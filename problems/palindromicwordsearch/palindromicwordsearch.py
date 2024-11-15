ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))

row, col = mii()

grid = [[c for c in input()] for _ in range(row)]

row_max = [[1 for _ in range(col)] for _ in range(row)]
col_max = [[1 for _ in range(col)] for _ in range(row)]
# rows

def test_row(row_i, center_i, even=False) -> bool:
    l, r = center_i - 1, center_i + 1
    
    if even:
        r += 1
    
    while l >= 0 and r < col and grid[row_i][l] == grid[row_i][r]:
        l -= 1
        r += 1

    length = r - l - 1
    
    for i in range(l+1, r):
        row_max[row_i][i] = max(row_max[row_i][i], length)

def test_col(col_i, center_i, even=False) -> bool:
    l, r = center_i - 1, center_i + 1
    
    if even:
        r += 1
    
    while l >= 0 and r < row and grid[l][col_i] == grid[r][col_i]:
        l -= 1
        r += 1

    length = r - l - 1
    
    for i in range(l+1, r):
        col_max[i][col_i] = max(col_max[i][col_i], length)


for i in range(row):
    for center in range(col-1):
        test_row(i, center)
        
        if grid[i][center] == grid[i][center+1]:
            row_max[i][center] = max(2, row_max[i][center])
            row_max[i][center+1] = max(2, row_max[i][center+1])
            test_row(i, center, even=True)


for j in range(col):
    for center in range(row-1):
        test_col(j, center)
        
        if grid[center][j] == grid[center+1][j]:
            col_max[center][j] = max(2, col_max[center][j])
            col_max[center+1][j] = max(2, col_max[center+1][j])
            test_col(j, center, even=True)

# for v in row_max:
#     print(*v)

# print()
# for v in col_max:
#     print(*v)
m = 0
for y in range(row):
    for x in range(col):
        m = max(row_max[y][x]*col_max[y][x], m)
print(m)