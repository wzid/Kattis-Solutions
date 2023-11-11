n = int(input())
f = input()
s = input()

su = 0
for i in range(len(f)):
    if f[i] == s[i]:
        su += 1

if su:
    print(su + ((len(s) - su) - abs(su - n)))
else:
    print(len(s) - n)