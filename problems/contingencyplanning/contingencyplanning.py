def permutation(n, c):
    value = 1
    for i in range(n - c + 1, n + 1):
        value *= i
    return value

n = int(input())
res = 0
for i in range(1, n + 1):
    res += permutation(n, i)
if res > 1000000000:
    print("JUST RUN!!")
else:
    print(res)