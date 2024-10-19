n = int(input())

real_items = list(map(int, input().split()))

graph = {}

m = int(input())
if m == 0:
    print('impossible')
    exit()

for i in range(m):
    a, b, d = map(int, input().split())
    if a not in graph:
        graph[a] = [(b, d)]
    else:
        graph[a].append((b, d))

    if b not in graph:
        graph[b] = [(a, d)]
    else:
        graph[b].append((a, d))


def dijkstra(graph, start):
    import heapq
    """
    Run dijkstra's shortest path for an adjacency list graph
    O(edges log(verts) )
    :param graph: Dict of graph in form graph[node] = [(next, cost) ... ]
          Adjacency list of tuples
    :param start: The node to start from
    :return: distances
    """
    dist = {}  # stores the minimum distances
    _items = {} # stores the items avaliable at that distance
    maxVal = float('inf')
    for node in graph.keys():  # each distance preset to inf
        dist[node] = maxVal
    dist[start] = 0  # distance to start set to 0
    _items[start] = real_items[start-1]
    unvisited = []  # heap of unvisited nodes
    from collections import defaultdict
    visited = defaultdict(list)
    visited[start] = [start]
    heapq.heappush(unvisited, (start, 0))  # init heap of form (node, cost)
    while unvisited:  # continue while unvisited nodes remain
        current_min, current_cost = heapq.heappop(unvisited)
        if current_cost == dist[current_min]:  # should be processing
            neighbors = graph[current_min]  
            # neighbors look like [(next, cost), (next, cost)]
            for neighbor in neighbors:
            # check all neighbors as cheapest option and add to heap
                
                tentative_value = dist[current_min] + neighbor[1]
                
                # print(tentative_value)
                if tentative_value < dist[neighbor[0]]:
                    dist[neighbor[0]] = tentative_value
                    
                    visited[neighbor[0]] = visited[current_min].copy()
                    if neighbor[0] in visited[current_min]:
                        _items[neighbor[0]] = _items[current_min]
                        # visited[neighbor[0]] = visited[current_min]
                    else:
                        _items[neighbor[0]] = _items[current_min] + real_items[neighbor[0]-1]
                        # visited[current_min].append(neighbor[0])
                        visited[neighbor[0]].append(neighbor[0])
                    
                    heapq.heappush(unvisited, (neighbor[0], dist[neighbor[0]]))

                    
                if tentative_value == dist[neighbor[0]]:
                    if neighbor[0] in visited[current_min]:
                        if _items[current_min] > _items[neighbor[0]]:
                            _items[neighbor[0]] = _items[current_min]
                            heapq.heappush(unvisited, (neighbor[0], dist[neighbor[0]]))
                            visited[neighbor[0]] = visited[current_min].copy()

                    elif _items[current_min] + real_items[neighbor[0]-1] >= _items[neighbor[0]]:
                            heapq.heappush(unvisited, (neighbor[0], dist[neighbor[0]]))
                            _items[neighbor[0]] = _items[current_min] + real_items[neighbor[0]-1]
                        
                            visited[neighbor[0]] = visited[current_min].copy()
                            visited[neighbor[0]].append(neighbor[0])

    # print(f'{visited=}')
    return (dist, _items)


dist, _items = dijkstra(graph=graph, start=1)

if n in dist and n in _items:
    # print(f'{_items=}')
    print(dist[n], _items[n])
else:
    print('impossible')