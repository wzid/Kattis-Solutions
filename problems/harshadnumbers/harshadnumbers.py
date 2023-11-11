n = int(input())
m = n
while True:
    h = str(m)
    s = 0
    for c in h:
        s += int(c)
    
    if m % s == 0:
        print(m)
        break
    m += 1