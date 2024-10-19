
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    jack = set()
    both_own = 0
    for i in range(n):
        jack.add(int(input()))

    for i in range(m):
        val = int(input())
        if val in jack:
            both_own += 1

    print(both_own)