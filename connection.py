import random
from collections import defaultdict
from adjacencyList import AdjacencyList


class Graph:

    def __init__(self):
        self.V = 5
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def getEdge(self, u):
        return self.graph[u]

    def DFS(self, v, visited):
        visited[v] = 1

        for i in self.graph[v]:
            if visited[i] == 0:
                self.DFS(i, visited)

    def getTranspose(self):
        g = Graph()

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)

        return g

    def isStrong(self):
        visited = {'BER': 0, 'SEO': 0, 'LDN': 0, 'TKY': 0, 'NY': 0}
        self.DFS('SEO', visited)

        if any(visited[i] == 0 for i in visited):
            return False

        reverseGraph = self.getTranspose()
        visited = {'BER': 0, 'SEO': 0, 'LDN': 0, 'TKY': 0, 'NY': 0}
        reverseGraph.DFS('SEO', visited)

        if any(visited[i] == 0 for i in visited):
            return False

        return True

    def randomGraph(self):
        adList = AdjacencyList.getOriList()
        graph = Graph()

        for origin in adList:
            for destination in adList[origin]:
                graph.addEdge(origin, destination)

        while graph.isStrong() is False:
            origin = random.choice(list(adList))
            destination = random.choice(list(adList))

            if origin == destination or destination in graph.getEdge(origin):
                continue

            graph.addEdge(origin, destination)

        return graph