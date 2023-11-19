from sys import stdin
l = []

for line in stdin:
    line = line.rstrip()
    l.append(line)

m = len(max(l, key=len))

ans = 0
for i in range(len(l)-1):
    ans += (len(l[i]) - m) ** 2

print(ans)