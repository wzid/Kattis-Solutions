

ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))


def getDigits(x, k):
    x = str(x)
    while len(x) < k:
        x = "0" + x
    return x

k, n = mii()
goodNums = []
codes = []
for _ in range(n):
    codes.append(input())


for i in range(10 ** k):
    dd = getDigits(i, k)
    good = True
    # print(dd)
    for code in codes:
        di = 0
        for j in range(len(code)):
            if code[j] == dd[di]:
                di += 1
                if di == k:
                    break
        if di < k:
            good = False
            break

    if good:
        goodNums.append(dd)

print(len(goodNums))
for gn in goodNums:
    print(gn)