# n, x = map(int, input().split())
n, x = map(int, input().split())

l = list(map(int, input().split()))
for i in range(n):
    if l[i] == x:
        if i == 0:
            print('fyrst')
        elif i == 1:
            print('naestfyrst')
        else:
            print(str(i+1), 'fyrst')
        exit()