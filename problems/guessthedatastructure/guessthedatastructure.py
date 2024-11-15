import sys
from collections import deque
import heapq
for line in sys.stdin:
    n = int(line.strip())
    r = []
    
    stack = []
    queue = deque()
    pq = []
    isStack = True
    isQueue = True
    isPQ = True
    for i in range(n):
        a, b = map(int, input().split())
        if a == 1:
            stack.append(b)
            queue.append(b)
            heapq.heappush(pq, -b)
        else:
            x1 = -1
            if stack:
                x1 = stack.pop()
            if x1 != b:
                isStack = False
            x2 = -1
            if queue:
                x2 = queue.popleft()
            if x2 != b:
                isQueue = False
            x3 = -1
            if pq:
                x3 = -heapq.heappop(pq)
            if x3 != b:
                isPQ = False
    
    s = isStack + isQueue + isPQ
    if s > 1:
        print('not sure')
    elif s == 0:
        print('impossible')
    elif isQueue:
        print('queue')
    elif isPQ:
        print('priority queue')
    elif isStack:
        print('stack')