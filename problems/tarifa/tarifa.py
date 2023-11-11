x = int(input())
n = int(input())
left = 0
for i in range(n):
    p = int(input())
    left += x - p

print(left + x)