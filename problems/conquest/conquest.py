n, m = map(int, input().split())

adj_matrix = [[] for _ in range(n)]
army_size = {}

for i in range(m):
    u, v = map(int, input().split())
    # normalize the input since its not 0-indexed
    u -= 1
    v -= 1

    adj_matrix[u].append(v)
    adj_matrix[v].append(u)

for i in range(n):
    army_size[i] = int(input())


import heapq

visited = set()
to_check = []

to_check.append((army_size[0], 0))

while len(to_check) > 0:

    _, s = heapq.heappop(to_check)
    if s not in visited:
        visited.add(s)
        

        if army_size[s] < army_size[0]:
            army_size[0] += army_size[s]

        for neighbor in adj_matrix[s]:
            if neighbor not in visited:
                heapq.heappush(to_check, (army_size[neighbor], neighbor))
    
    if to_check and army_size[to_check[0][1]] >= army_size[0]:
        break

print(army_size[0])