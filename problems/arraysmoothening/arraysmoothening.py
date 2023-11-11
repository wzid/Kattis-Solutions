from collections import Counter
import heapq

n, k = map(int, input().split())
array = list(map(int, input().split()))

occurrences = Counter(array)
max_heap = [-count for count in occurrences.values()]
heapq.heapify(max_heap)

while k > 0:
    new_count = heapq.heappop(max_heap) + 1
    heapq.heappush(max_heap, new_count)
    k -= 1

print(-max_heap[0])