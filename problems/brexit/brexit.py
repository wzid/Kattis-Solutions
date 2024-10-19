countries, parterships, home_country, first_country_to_leave = map(int, input().split())

trading_partner_total_count = {}

graph = {}

for i in range(parterships):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)

for country, s in graph.items():
    trading_partner_total_count[country] = len(s)

from queue import Queue
queue = Queue()

queue.put(first_country_to_leave)

for partner in graph[first_country_to_leave]:
    queue.put(partner)
graph[first_country_to_leave].clear()

while not queue.empty():
    if len(graph[home_country]) <= trading_partner_total_count[home_country] / 2:
        print('leave')
        exit()

    curr_country = queue.get()
    if not graph[curr_country]:
        continue

    remove = set()
    for partner in graph[curr_country]:
        if curr_country not in graph[partner]:
            remove.add(partner)
    
    if remove:
        graph[curr_country] -= remove
    
    if len(graph[curr_country]) <= trading_partner_total_count[curr_country] / 2:
        for partner in graph[curr_country]:
            graph[partner].remove(curr_country)
            if len(graph[partner]) <= trading_partner_total_count[partner] / 2:
                queue.put(partner)
        
        graph[curr_country].clear()


if len(graph[home_country]) <= trading_partner_total_count[home_country] / 2:
    print('leave')
else:
    print('stay')