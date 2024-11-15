ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))

p, t = mii()

letters = set(map(chr,range(65,65+p)))

unis = set()
c = 0
for _ in range(t):
    x = input()
    x_sort = sorted(x)
    # print(x, x_sort)
    if x_sort[-1] in letters and len(set(x)) == len(x):
        unis.add(x)

unis = list([set(x) for x in unis])

# print(unis)
m = 0
for i in range(len(unis)):
    take = letters.copy()
    take.difference_update(unis[i])
    _m = 1
    for j in range(len(unis)):
        if i == j:
            continue
        if unis[j].issubset(take):
            take.difference_update(unis[j])
            _m += 1
    m = max(m, _m)
print(m)