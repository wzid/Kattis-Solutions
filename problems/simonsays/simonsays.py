n = int(input())

for i in range(n):
    s = input().split('Simon says ')
    if s[0] == '':
        print(s[-1])