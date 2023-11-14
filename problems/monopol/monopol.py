n = int(input())
hotels = list(map(int, input().split()))

possible = 36

ways = [0,0,1,2,3,4,5,6,5,4,3,2,1,0]

for hot in hotels:
  possible -= ways[hot]
print(1-possible/36)