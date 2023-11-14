n = int(input())
rows = ['w'] * n
cols = ['g'] * n
for i in range(n):
    s = input()
    rows[i] = s
    for j in range(n):
        if i == 0:
            cols[j] = s[j]
        else:
            cols[j] += s[j]

w_count = rows[0].count('W')
w_count2 = cols[0].count('W')
for i in range(n):
    if rows[i].count('W') != w_count:
        print(0)
        exit()
    if cols[i].count('W') != w_count2:
        print(0)
        exit()
    if 'WWW'in cols[i] or 'WWW' in rows[i] or 'BBB' in rows[i] or 'BBB' in cols[i]:
        print(0)
        exit()
print(1)