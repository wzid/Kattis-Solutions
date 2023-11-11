n = int(input())

while n >= 10:
    s = str(n)
    b = 1
    for c in s:
        if c != '0':
            b *= int(c)
    n = b
print(n)