n = int(input())

nums = list(map(int, input().split()))
skip_ones = [0 for _ in range(n)]
ones = 0
one_i = -1
for i, x in enumerate(nums):
    if x == 1:
        if ones:
            ones += 1
        else:
           ones = 1
           one_i = i
    elif ones:
        for j in range(ones):
            skip_ones[one_i + j] = ones - j
        # skip_ones[one_i] = ones
        ones = 0
if ones:
    for j in range(ones):
        skip_ones[one_i + j] = ones - j - 1

n = len(nums)

# print(skip_ones)

prefix = nums.copy()
prefix[0] = 0
for i in range(1, n):
    prefix[i] = nums[i-1] + prefix[i-1]

l = 0
count = 0
while l < n - 1:
    s_t = nums[l]
    m = nums[l]
    
    r = l + 1
    while r < n:
        if skip_ones[r]:
            if m <= s_t + skip_ones[r] and m > s_t:
                count += 1
                s_t += skip_ones[r]
                r += skip_ones[r]
            else:
                s_t += skip_ones[r]
                r += skip_ones[r]
        else:
            m *= nums[r]
            s_t += nums[r]
            
            if s_t == m:
                # print(l, r, s_t)
                count += 1
            
            if m > prefix[n-1] - prefix[l] + nums[n-1]:
                break
            r += 1

    l += 1

print(count)