s = 'PER'
inp = input()
days = 0
for i, c in enumerate(inp):
    if s[i%3] != c:
        days += 1
print(days)