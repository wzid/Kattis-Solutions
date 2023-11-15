h, w = map(int, input().split())
d = {'.': 20, 'O': 10, '\\': 25, '/': 25, 'A': 35, '^': 5, 'v': 22}
summ = 0
for i in range(h):
    s = input()
    for c in s:
        summ += d[c]
print(summ)
