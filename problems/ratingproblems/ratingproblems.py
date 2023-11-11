n, k = map(int, input().split())

d = 0
for i in range(k):
    d += int(input())

left = n - k

minumum = ((-3*left) + d) / n
max = ((3*left) + d) / n
print(minumum, max)