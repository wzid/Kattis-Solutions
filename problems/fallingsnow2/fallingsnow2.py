h, w = map(int, input().split())

grid = []
column_to_s_count = {i:0 for i in range(w)}

for _ in range(h):
    x = input()
    for i, c in enumerate(x):
        if c == 'S':
            column_to_s_count[i] += 1

for j in range(h):
    res = ''
    for i in range(w):
        if column_to_s_count[i] >= h-j:
            res += 'S'
        else:
            res += '.'
    print(res)