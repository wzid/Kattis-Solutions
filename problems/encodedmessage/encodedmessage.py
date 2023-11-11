import math
n = int(input())
for i in range(n):
    s = input()
    arr_length = int(math.sqrt(len(s)))
    l = []
    for x in range(arr_length):
        for j in range(1, arr_length+1):
            l.append(s[(j*arr_length)-x-1])
    print(''.join(l))
