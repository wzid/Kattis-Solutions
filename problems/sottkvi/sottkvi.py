n, k, d = map(int, input().split())

f = 0
for i in range(1, n+1):
    x = int(input())
    if 14-((d-x) + k) <= 0:
        f += 1
        
print(f)