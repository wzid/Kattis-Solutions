G, T, N =map(int, input().split())
w = list(map(int, input().split()))

print(int((G-T)*.9)-sum(w))