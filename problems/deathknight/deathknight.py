n = int(input())

su = 0
for i in range(n):
    s = input()
    if 'CD' not in s:
        su += 1
print(su)
