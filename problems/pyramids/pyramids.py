n = int(input())

line = 1
i = 0
while n >= line * line:
    n -= line * line
    i += 1
    line += 2

print(i)