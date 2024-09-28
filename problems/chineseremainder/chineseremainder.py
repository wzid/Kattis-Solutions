def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x += m0
    return x

t = int(input())

for _ in range(t):
    a, n, b, m = map(int, input().split())
    K = n * m
    first = (((a * m) % K) * mod_inverse(m, n)) % K
    second = (((b * n) % K) * mod_inverse(n, m)) % K
    x = (first + second) % K
    print(x, K)