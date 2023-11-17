remove_letters = input()
s = input().split()

res = []
for word in s:
    found = False
    for c in remove_letters:
        if c in word:
            res.append('*'*len(word))
            found = True
            break
    if not found:
        res.append(word)
print(*res)
