n = int(input())

for i in range(n):
    t = int(input())
    l = list(map(int, input().split()))
    optimal = (max(l) - min(l)) * 2
    print(optimal)