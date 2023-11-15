n = int(input())
d = {}
for i in range(n):
    s = input().split()
    name = s[0]
    like = int(s[1])
    date = s[2]
    if date in d:
        curr_like, curr_name = d[date]
        if like > curr_like:
            d[date] = (like, name)
    else:
        d[date] = (like, name)
print(len(d))

names = [item[1][1] for item in d.items()]
names.sort()
for name in names:
    print(name)