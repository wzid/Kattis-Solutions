a, b = map(int, input().split())

if b < a:
    a, b = b, a

for i in range(a+1, b+2):
    print(i)