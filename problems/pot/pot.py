n = int(input())

ssum = 0
for i in range(n):
    s = input()
    exp = int(s[-1])
    num = int(s[:-1])
    ssum += num**exp
print(ssum)