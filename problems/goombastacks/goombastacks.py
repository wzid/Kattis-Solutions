n = int(input())
ssum=0
for i in range(n):
    g, b = map(int,input().split())
    ssum += g
    if ssum < b:
        print("impossible")
        exit()
    
    
print("possible")