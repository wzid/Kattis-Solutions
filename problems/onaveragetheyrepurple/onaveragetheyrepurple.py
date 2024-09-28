def bfs(graph, source, target):
    """
    Find a node in a graph
    :param graph: An adjacency list stored in a dict: graph[start] = [list of destination nodes]
    :param source: starting node
    :param target: destination node
    :return: whether it is in the graph
    """
    from collections import deque
    visited = {}
    queue = deque()
    found = False

    visited[source] = 0
    queue.append(source)

    while len(queue) > 0:          # Creating loop to visit each node
        m = queue.popleft()

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited[neighbor] = 1 + visited[m]
                queue.append(neighbor)
                if neighbor == target:
                    return visited[m] + 1

    return False

n, m = map(int, input().split())
g = {}
for i in range(m):
    from_, to = map(int, input().split())
    if to not in g:
        g[to] = []
    if from_ not in g:
        g[from_] = []
    g[from_].append(to)
    g[to].append(from_)

result = bfs(g, 1, n)
print(max(0, result - 1))