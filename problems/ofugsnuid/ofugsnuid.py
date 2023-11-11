n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

for i in range(1, n+1):
    print(l[-i])
