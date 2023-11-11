n = int(input())

a = list(map(int, input().split()))
steps = []

while True:
    maxx, maxx_index = 0, -1
    minn, minn_index = 9999, -1

    for i in range(len(a)):
        if a[i] == 0:
            continue
        if a[i] > maxx:
            if maxx != 0 and maxx < minn:
                minn = maxx
                minn_index = maxx_index
            maxx = a[i]
            maxx_index = i
        elif a[i] < minn:
            minn = a[i]
            minn_index = i
    
    if maxx == 0 and minn == 9999:
        print('yes')
        for step in steps:
            print(step)
        break
    elif maxx == 0 or minn == 9999:
        print('no')
        break

    steps.append(str(maxx_index+1) + ' ' +  str(minn_index+1))

    a[minn_index] -= 1
    a[maxx_index] -= 1