n = int(input())
for i in range(n):
    junk, c = input().split(" ")
    a, b = map(int, c.split("/"))
    if a == b == 1:
        print(i+1, 1)
        continue
    dirs = []
    while a != b:
        if a < b:
            b -= a
            dirs.insert(0, "0")
        elif a > b:
            a -= b
            dirs.insert(0, "1")

    n = 2 ** len(dirs)  + int("0b" + "".join(dirs), 2)
    print(i+1,n)
