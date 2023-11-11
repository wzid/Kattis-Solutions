n = int(input())

l = list(map(int, input().split()))
sm = float('inf')
sm_i = -1
for i in range(n):
    if l[i] < sm:
        sm = l[i]
        sm_i = i
print(sm_i)