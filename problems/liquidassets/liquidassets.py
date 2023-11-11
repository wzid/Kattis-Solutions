
input()

s = input().split()
res = []
v = 'aeiou'
for j in range(len(s)):
    word = s[j]
    res.append('')
    last = ''
    ress = ''
    for c in word:
        if last != c:
            ress += c
        last = c

    res[j] += ress[0]
    if len(ress) > 2:
        for i in range(1, len(ress)-1):
            if ress[i] not in v:
                res[j] += ress[i]
    if len(ress) > 1:
        res[j] += ress[-1]


final = ''
for wor in res:
    if wor:
        final += wor + ' '


print(final[:-1])