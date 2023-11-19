n = int(input())

res = 0
for i in range(n):
    s = input().lower()
    if 'rose' in s or 'pink' in s:
        res += 1
if res:
    print(res)
else:
    print('I must watch Star Wars with my daughter')
    