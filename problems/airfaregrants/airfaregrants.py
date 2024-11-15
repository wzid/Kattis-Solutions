

ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))

n = ii()
nums = []
for _ in range(n):
    nums.append(ii())

a = min(nums)
b = max(nums)

print(int(max(0, a-b/2)))