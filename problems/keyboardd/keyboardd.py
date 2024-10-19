s = input()
s2 = input()

res = set()
last = ''

index = 0
for c in s:
    while c != s2[index] and s2[index] == last:
        res.add(s2[index])
        index += 1
    else:
        index += 1
    last = c

while index < len(s2) and s2[index] == last:
    res.add(s2[index])
    index += 1

print(''.join(res))