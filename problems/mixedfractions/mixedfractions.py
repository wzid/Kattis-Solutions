n, m = map(int, input().split())
while n != 0 or m != 0:
    print(n//m, n % m, '/', m)
    n, m = map(int, input().split())