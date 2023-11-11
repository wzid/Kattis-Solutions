i = input()

b = i.count('(') == 1 and i.count(')')


if b:
    i = i.split('()')
    if len(i[0]) == len(i[1]):
        print('correct')
    else:
        print('fix')
else:
    print('fix')