n = int(input())
t = 0
for i in range(n):
    a, b = map(float, input().split(' '))
    t += a * b

print(t)