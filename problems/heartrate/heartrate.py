n = int(input())

for i in range(n):
    inp = input().split()
    b = int(inp[0])
    p = float(inp[1])
    
    bpm = (60*b)/p
    minn = (60*(b-1)) / p
    maxx = (60*(b+1)) / p
    print(minn, bpm, maxx)
    