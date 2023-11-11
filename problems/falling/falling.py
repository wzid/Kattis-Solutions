D = int(input())
d = {}
for i in range(200001):
    v = i**2
    find = v - D
    if find in d:
        print(d[find], i)
        exit()
    d[v] = i
print('impossible')