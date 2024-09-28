n = int(input())
m = 0
m_n = ''
for i in range(n):
    x = input().split()
    a, b = x[0], int(x[1])
    if b > m:
        m = b
        m_n = a

print(m_n)
