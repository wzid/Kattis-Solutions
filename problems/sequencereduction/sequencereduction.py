n = int(input())
l = [int(input()) for _ in range(n)][::-1]
cost = 0
for i in range(n-1):
    cost += max(l[i:i+2])
print(cost)