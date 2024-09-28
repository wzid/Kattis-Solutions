n, m = map(int, input().split())

s = set()
s = set(input().split())
for i in range(n-1):
    l = input().split()
    s = s.intersection(l)

print(len(s))
s = sorted(list(s))
for v in s:
    print(v)