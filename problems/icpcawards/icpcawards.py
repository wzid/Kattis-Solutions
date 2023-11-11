n = int(input())
d = {}

for i in range(n):
    uni, name = input().split()
    if uni not in d:
        d[uni] = name
    
    if len(d) == 12:
        break
for k, v in d.items():
    print(k,v)
