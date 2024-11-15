from collections import defaultdict
import heapq
from itertools import permutations
def dijkstra(graph, start, end, n):
    dist = [float('inf') for _ in range(n)]
    dist[start] = 0  # distance to start set to 0
    unvisited = [(0, start)]  # heap of unvisited nodes
    while unvisited:  # continue while unvisited nodes remain
        current_cost, current_min = heapq.heappop(unvisited)
        if current_min == end:
            return current_cost
        
        if current_cost == dist[current_min]:
            # check all neighbors as cheapest option and add to heap
            for neighbor in graph[current_min]:
                tentative_value = dist[current_min] + neighbor[1]
                if tentative_value < dist[neighbor[0]]:
                    dist[neighbor[0]] = tentative_value
                    heapq.heappush(unvisited, (dist[neighbor[0]], neighbor[0]))
    return dist[end]
 

n, m = map(int, input().split())



graph = [[] for _ in range(n)]

for i in range(m):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, t))
    graph[b].append((a, t))

db_cities = list(set(int(x)-1 for x in input().split()))


# we have permutations of the shortest distance to each one

# [(a, b)] = distance
distance = {}
distance[(0,0)] = 0
for i in range(len(db_cities)):
    city_i = db_cities[i]
    for j in range(i+1, len(db_cities)):
        city_j = db_cities[j]
        
        if (city_i, city_j) in distance:
            continue

        if city_i == city_j:
            distance[(city_i,city_j)] = 0
            continue


        dis = dijkstra(graph, city_i, city_j, n)
        
        if dis >= float('inf'):
            print(-1)
            exit()

        distance[(city_i,city_j)] = dis
        
        distance[(city_j,city_i)] = dis

# since we start at city 1 (0 because 0 indexed)
for i in range(len(db_cities)):
    if (city_i := db_cities[i]) != 0 and (0, city_i) not in distance:
        distance[(0, city_i)] = dijkstra(graph, 0, city_i, n)


combos = list(permutations(db_cities, len(db_cities)))
m = float('inf')
for combo in combos:
    curr_dis = distance[(0, combo[0])]
    for i in range(len(combo)-1):
        curr_dis += distance[(combo[i], combo[i+1])]
    m = min(m, curr_dis)

if m >= float('inf'):
    print(-1)
else:
    print(m)