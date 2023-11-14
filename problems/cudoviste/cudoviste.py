R, C = map(int, input().split())

m = []
for i in range(R):
    m.append(list(input()))
    
smashed = [0,0,0,0,0]
for i in range(R - 1):
    for j in range(C - 1):
        spaces = [m[i][j], m[i][j+1], m[i+1][j], m[i+1][j+1]]
        if '#' in spaces:
            continue
        smashed[spaces.count('X')] += 1
for s in smashed:
    print(s)