y = [i for i in input().split()]
n = int(y[0])
c = str(y[1])

d = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
nd = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}

s = 0
for i in range(4*n):
    full = input()
    left = full[0]
    right = full[1]
    
    if right == c:
        s += d[left]
    else:
        s += nd[left]
        
print(s)