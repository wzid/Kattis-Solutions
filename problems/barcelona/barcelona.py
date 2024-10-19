n, k = map(int, input().split())

ind = list(map(int, input().split())).index(k)

if ind == 0:
    print('fyrst')
elif ind == 1:
    print('naestfyrst')
else:
    print(ind+1, 'fyrst')