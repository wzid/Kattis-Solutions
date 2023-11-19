a,b,c = map(int, input().split())

l = []

if a+b == c:
    l.append(f'{a}+{b}={c}')
if a-b==c:
    l.append(f'{a}-{b}={c}')
if a//b ==c:
    l.append(f'{a}/{b}={c}')
if a*b ==c:
    l.append(f'{a}*{b}={c}')
if a==b+c:
    l.append(f'{a}={b}+{c}')
if a==b-c:
    l.append(f'{a}={b}-{c}')
if a==b//c:
    l.append(f'{a}={b}/{c}')
if a == b*c:
    l.append(f'{a}={b}*{c}')
    
print(l[0])
        

