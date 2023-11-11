n = int(input())
curr = int(input())
for i in range(n-1):
    curr = (int(input()) + curr) - 1
print(curr)
