n = int(input())

l = list(map(int, input().split()))

ll = [0] * (n-1)
for i, ind in enumerate(l):
    ll[ind] = i+2

ll = [1] + ll
print(*ll)