c = [int(x) for i in input().split('-') for x in i]

y = c[0]*4 + c[1]*3 + c[2]*2 + c[3]*7 + c[4]*6 + c[5]*5 + c[6]*4 + c[7]*3 + c[8]*2 + c[9]*1

if y % 11 == 0:
    print(1)
else:
    print(0)