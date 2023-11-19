n = int(input())

while n != -1:
    last_t = 0
    distance = 0
    for i in range(n):
        s, t = map(int, input().split())
        distance += (t - last_t) * s
        last_t = t
    print(f'{distance} miles')
        
    n = int(input())
