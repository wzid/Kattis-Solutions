n, y = map(int, input().split())

s = set()
for i in range(y):
    k = int(input())
    if k < n:
        s.add(k)

for i in range(n):
    if i not in s:
        print(i)
 
print(f'Mario got {len(s)} of the dangerous obstacles.')