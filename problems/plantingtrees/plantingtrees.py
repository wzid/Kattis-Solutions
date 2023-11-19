n = int(input())
trees = list(map(int, input().split()))
trees.sort()

ma = 0
for i, days in enumerate(trees):
  ma = max(ma, days-i+n+1)

print(ma)