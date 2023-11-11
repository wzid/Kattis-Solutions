n = input()

lines = [['' for _ in range(4)] for _ in range(4)]
for i, c in enumerate(n):
    b = str(bin(int(c))[2:])
    b = ('0' * (4 - len(b))) + b

    for j in range(3, -1, -1):
        lines[j][i] = '*' if b[j] == '1' else '.'
    

for line in lines:
    print(f'{line[0]} {line[1]}   {line[2]} {line[3]}')
