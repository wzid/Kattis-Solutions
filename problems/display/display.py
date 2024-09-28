l = input()

one = [
    "    +",
    "    |",
    "    |",
    "    +",
    "    |",
    "    |",
    "    +",
]
two = [
    '+---+',
    '    |',
    '    |',
    '+---+',
    '|    ',
    '|    ',
    '+---+',
]

three = [
    '+---+',
    '    |',
    '    |',
    '+---+',
    '    |',
    '    |',
    '+---+',
]

four = [
    '+   +',
    '|   |',
    '|   |',
    '+---+',
    '    |',
    '    |',
    '    +'
]

five = [
    '+---+',
    '|    ',
    '|    ',
    '+---+',
    '    |',
    '    |',
    '+---+'
]

six = [
    '+---+',
    '|    ',
    '|    ',
    '+---+',
    '|   |',
    '|   |',
    '+---+'
]

seven = [
    '+---+',
    '    |',
    '    |',
    '    +',
    '    |',
    '    |',
    '    +',
]

eight = [
    '+---+',
    '|   |',
    '|   |',
    '+---+',
    '|   |',
    '|   |',
    '+---+',
]

nine = [
    '+---+',
    '|   |',
    '|   |',
    '+---+',
    '    |',
    '    |',
    '+---+',
]

zero = [
    '+---+',
    '|   |',
    '|   |',
    '+   +',
    '|   |',
    '|   |',
    '+---+',
]

numbers = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine,
    0: zero
}

while l != "end":
    nums = [int(l[0]), int(l[1]), int(l[3]), int(l[4])]
    
    for index in range(0, 7):
        line = ''
        for i, n in enumerate(nums):
            line += numbers[n][index]

            if i != len(nums)-1:
                line += '  '
            if i == 1 and (index == 2 or index == 4):
                line += 'o  '
            elif i == 1:
                line += '   '
        print(line)

    l = input()
    print()
    print()

print('end')