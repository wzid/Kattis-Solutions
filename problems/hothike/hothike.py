n = int(input())

l = list(map(int, input().split()))
b = [(max(l[i], l[i+2]), i) for i in range(n-2)]

t, d = min(b)
print(d+1, t)
