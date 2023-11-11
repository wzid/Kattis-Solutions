a = input()
n = input()

it = len(n) // 3
s = ''
for i in range(it):
    i = i*3
    g = n[i:i+3]
    s += a[int(g)-1]
print(s)