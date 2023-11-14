n = int(input())
lines = []

for i in range(n):
    row = input().split()
    j = 0
    for c in row:
        if int(c) > 0:
            lines.append([i+1, j+1, c])
        j += 1

print(len(lines))
for line in lines:
    print(*line)