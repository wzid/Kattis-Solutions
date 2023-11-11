n = int(input())

for i in range(n):
    r, e, c = map(int, input().split())
    result = e - c
    if r < result:
        print('advertise')
    elif r > result:
        print('do not advertise')
    elif r == result:
        print('does not matter')