from math import factorial as fc
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    m-=1
    print(fc(n) // fc(m) // fc(n-m))