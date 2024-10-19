n = int(input())

t = 7
for i in range(n):
    x = input()
    if x == 'Skru op!':
        if t != 10:
            t += 1
    else:
        if t != 0:
            t -= 1
print(t)