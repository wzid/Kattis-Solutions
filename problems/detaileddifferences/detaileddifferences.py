n = int(input())

for i in range(n):
    a = input()
    b = input()
    s = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            s += '*'
        else:
            s += '.'
    print(a)
    print(b)
    print(s)
    print()