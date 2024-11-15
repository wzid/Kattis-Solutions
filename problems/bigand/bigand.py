
ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))
import heapq
n, d, l = mii()
h = mii()

heapq.heapify(h)
while len(h) >= 2:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    
    c = max(a, b) + d
    heapq.heappush(h, c)

x = heapq.heappop(h)
print(x + l)