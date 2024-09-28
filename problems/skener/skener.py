R, C, Z_r, Z_c = map(int, input().split())

new = []
for i in range(R):
    x = input()
    new_s = ''
    for c in x:
        for i in range(Z_c):
            new_s += c
    
    for i in range(Z_r):
        new.append(new_s)

for s in new:
    print(s)