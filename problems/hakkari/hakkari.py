# n, m = map(int, input().split())
n, m = map(int, input().split())

coords = []
for i in range(n):
    x = input()
    for j, c in enumerate(x):
        if c == '*':
            coords.append((i+1, j+1))

print(len(coords))
for c in coords:
    print(c[0], c[1])