n = int(input())
l = []
for i in range(1, n+1):
    if i % 2:
        l.append(input())
    else:
        input()

for j in l:
    print(j)
        