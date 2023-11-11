volume = 7

n = int(input())

for i in range(n):
    c = input()
    if c == 'Skru op!':
        if volume != 10:
            volume += 1
    elif c == 'Skru ned!':
        if volume != 0:
            volume -= 1
print(volume)