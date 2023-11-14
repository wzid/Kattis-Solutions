l = list(input())

s = input().split()
d = {}
d2 = {}
ind = 0
if len(l) != len(s):
    print(False)
    exit()

for word in s:
    if ind > len(l) - 1:
        print(False)
        exit()
    if word in d:
        if d[word] != l[ind]:
            print(False)
            exit()
    else:
        if l[ind] in d2:
            print(False)
            exit()
        else:
            d[word] = l[ind]
            d2[l[ind]] = word

    ind += 1
    if ind > len(l) - 1:
        ind = 0
        
print(True)