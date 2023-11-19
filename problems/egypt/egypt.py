l = list(map(int, input().split()))

while l[0] != 0 or l[1] != 0 or l[2] != 0:
    l.sort()
    
    if l[0]**2 + l[1]**2 == l[2]**2:
        print("right")
    else:
        print("wrong")

    l = list(map(int, input().split()))