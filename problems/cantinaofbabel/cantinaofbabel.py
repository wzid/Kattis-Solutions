from collections import deque, defaultdict

class StrongConnected:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, source):
        visited = {}
        stack = deque()
        visited[source] = True
        stack.append(source)
        while len(stack) > 0:  # Creating loop to visit each node
            m = stack.popleft()
            for neighbor in self.graph[m]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    stack.append(neighbor)
        return visited

    def transpose(self):
        g = {}
        for i in self.graph:
            for j in self.graph[i]:
                if j not in g:
                    g[j] = [i]
                else:
                    g[j].append(i)
            if i not in g:
                g[i] = []
        return g

    def isSSC(self):
        s = list(self.graph.keys())[0]
        v1 = self.bfs(s)
        old = self.graph
        self.graph = self.transpose()
        v2 = self.bfs(s)
        self.graph = old
        if set(v1) == set(v2):
            return True
        else:
            return False

    def getSSC_Size(self, start):
        """
        Return the size of the strongly connected component that starts at start
        O(VE)
        :param start: The starting node
        :return: The size of the SCC that the start node is in
        """
        s = start
        v1 = set(self.bfs(s))
        old = self.graph
        self.graph = self.transpose()
        v2 = set(self.bfs(s))
        self.graph = old
        return len(v1.intersection(v2))


n = int(input())

adjacency_list = defaultdict(set)
speaks = defaultdict(str)
under = defaultdict(set)

start = ''
for i in range(n):
    y = input().split()
    
    name, langs = y[0], y[1:]
    speaks[name] = y[1]

    for l in langs:
        under[l].add(name)

for name, spoke_lang in speaks.items():
    for person in under[spoke_lang]:
        adjacency_list[name].add(person)

scc = StrongConnected(adjacency_list)

m = max(scc.getSSC_Size(k) for k in list(adjacency_list.keys()))

print(len(adjacency_list) - m)