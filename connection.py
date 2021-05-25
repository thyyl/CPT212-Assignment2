import random
from collections import defaultdict

from adjacencyList import AdjacencyList

class Graph:

    def __init__(self):
        #number of vertices
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

    def DFSUtil(self, u, color):
        # Change the color of the vertex to color 1
        color[u] = 1

        # for neighbour vertex that is connected to vertex
        for v in self.graph[u]:
            # if the color of the neighbour vertex is 1 return true
            if color[v] == 1:
                return True
            # if the color of the neighbour vertex is 0 and DFSUtil is also true, return true
            if color[v] == 0 and self.DFSUtil(v, color) == True:
                return True

        # Change the color of the vertex to 2 and return false
        color[u] = 2
        return False

    # Function to determine whether the graph is cyclic
    def isCyclic(self):
        # Color 0 means the vertex haven't been visited
        # Color 1 means the vertex is being process in DFSUtil but not ended
        # Color 2 means the vertex is fully visited
        # Initialize all the vertex to color 0
        color = {'BER': 0, 'SEO': 0, 'LDN': 0, 'TKY': 0, 'NY': 0}

        # Do DFS traversal beginning with all vertices
        for i in range(self.V):
            for city in list(self.graph):
                if (color[i] == 0 for i in color):
                    if self.DFSUtil(city, color) == True:
                        return True
        return False

    # only strongly connected
    def randomGraph(self, function):
        adList = AdjacencyList.getOriList()
        graph = Graph()

        for origin in adList:
            for destination in adList[origin]:
                graph.addEdge(origin, destination)

        if function == 'Strong Connectivity':
            while graph.isStrong() is False:
                origin = random.choice(list(adList))
                destination = random.choice(list(adList))

                if origin == destination or destination in graph.getEdge(origin):
                    continue

                graph.addEdge(origin, destination)

        elif function == 'Cycle Detection':
            while graph.isCyclic() is False:
                origin = random.choice(list(adList))
                destination = random.choice(list(adList))

                if origin == destination or destination in graph.getEdge(origin):
                   continue

                graph.addEdge(origin, destination)

        return graph
