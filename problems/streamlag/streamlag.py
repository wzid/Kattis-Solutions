# Data inputs
n = int(input())
frames = [0] * n
for _ in range(n):
  t, i = map(int, input().split())
  frames[i-1] = t 

lag = 0
currTime = 0
for i, frameTime in enumerate(frames):
  if frameTime <= currTime+1:
    currTime += 1
  else:
    lag += (frameTime - currTime) - 1
    currTime = frameTime

print(lag)
