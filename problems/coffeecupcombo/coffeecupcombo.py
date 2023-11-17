input()
s = input()
cups = 0
lectures = 0
for c in s:
    if c == '1':
        lectures += 1
        cups = 2
    elif c == '0' and cups > 0:
        cups -= 1
        lectures += 1
print(lectures)
    