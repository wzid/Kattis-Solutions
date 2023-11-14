n = int(input())

for i in range(n):
    imported = 0
    nums = list(map(int, input().split()))
    nums.pop()
    curr = 1
    for n in nums:
        if n > curr * 2:
            imported += n - curr * 2
        curr = n
    print(imported)