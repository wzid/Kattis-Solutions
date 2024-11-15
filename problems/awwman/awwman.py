t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a, b, d = map(int, input().split())
    get_to_cave_time = b - a
    leave_time = b + d + get_to_cave_time
    if leave_time % (n+1) > n-m:
        print('NO')
    else:
        print('YES')