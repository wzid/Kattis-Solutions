s = input()
n = len(s)
d = {'P': [], 'K': [], 'H': [], 'T': []}

for i in range(3, n+3, 3):
    sub = s[i-3:i]
    suit = sub[0]
    num = int(sub[1:])

    if num in d[suit]:
        print('GRESKA')
        exit()
    
    d[suit].append(num)


for k, v in d.items():
    d[k] = 13 - len(v)

print(d['P'], d['K'], d['H'], d['T'])