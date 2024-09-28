# n, m = map(int, input().split())
n, m = map(int, input().split())

l = []

for i in range(n):
    x = list(map(int, input().split()))
    l.append(x)

for i in range(len(l)):
    for j in range(len(l[i])):
        if i == len(l)-1 or j == len(l[i])-1 or i == 0 or j == 0:
            continue
    
        v = l[i][j]
        low = True
        
        if l[i+1][j] <= v or l[i-1][j] <= v or l[i][j-1] <= v or l[i][j+1] <= v:
            low = False
        
        if low:
            print('Jebb')
            exit()
print('Neibb')