s = input().split()
n = int(s[0])
k = int(s[1])
p = float(s[2])

if n * p < k:
    print('spela')
else:
    print('spela inte!')