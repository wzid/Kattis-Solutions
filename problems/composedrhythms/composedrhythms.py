k = int(input())

if k % 2 == 0:
    print(k//2)
    print('2 '*(k//2))
else:
    twos = 0
    while k % 3 != 0:
        twos += 1
        k -= 2
    print(k//3 + twos)
    print('3 '*(k//3) + '2 '*twos)