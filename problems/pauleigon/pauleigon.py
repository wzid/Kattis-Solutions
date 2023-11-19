n, p, q = map(int, input().split())

a = (p+q)// n

if a % 2 == 0:
    print("paul")
else:
    print("opponent")
