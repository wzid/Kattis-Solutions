import math

N, W, H = map(int, input().split())
hyp = math.sqrt(W*W+H*H)
for i in range(N):
    x = int(input())
    if x <= hyp:
        print('DA')
    else:
        print('NE')
    