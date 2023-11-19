import sys

d = {
    "**** ** ** ****": 0,
    "  *  *  *  *  *": 1,
    "***  *****  ***": 2,
    "***  ****  ****": 3,
    "* ** ****  *  *": 4,
    "****  ***  ****": 5,
    "****  **** ****": 6,
    "***  *  *  *  *": 7,
    "**** ***** ****": 8,
    "**** ****  ****": 9
}

max_l = 0
lines = [input() for _ in range(5)]

for line in lines:
    max_l = max(max_l, len(line))
    
lines = [line.ljust(max_l) for line in lines]

number = ""
for i in range(0, len(lines[0]), 4):
    digit = "".join(lines[j][i:i+3] for j in range(5))
    if not digit in d:
        print("BOOM!!")
        exit()
    number += str(d[digit])

number = int(number)
if number % 6 == 0:
    print("BEER!!")
    exit()
print("BOOM!!")