n = int(input())

expected = 1
l = []
for i in range(n):
    x = int(input())
    
    while x != expected:
        l.append(expected)
        expected += 1
    
    expected += 1

if len(l) == 0:
    print('good job')
else:
    for v in l:
        print(v)
