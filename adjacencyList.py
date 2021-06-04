class AdjacencyList:

    @staticmethod
    def getOriList():
        adjacencyList = {
            'SEO': [],
            'NY': ['SEO'],
            'TKY': ['BER', 'NY'],
            'LDN': ['SEO'],
            'BER': ['LDN'],
        }

        return adjacencyList

    def __init__(self):
        self.adjacencyList = {
            'SEO': [],
            'NY': ['SEO'],
            'TKY': ['BER', 'NY'],
            'LDN': ['SEO'],
            'BER': ['LDN'],
        }

        self.distance = {
            'SEO': {'NY': 11052, 'TKY': 1156, 'LDN': 8859, 'BER': 8127},
            'NY': {'SEO': 11052, 'TKY': 10847, 'LDN': 5571, 'BER': 6385},
            'TKY': {'NY': 10847, 'SEO': 1156, 'LDN': 9562, 'BER': 8918},
            'LDN': {'NY': 5571, 'TKY': 9562, 'SEO': 8859, 'BER': 932},
            'BER': {'NY': 6385, 'TKY': 8918, 'LDN': 932, 'SEO': 8127},
        }

    def resetList(self, resetList):
        self.adjacencyList = resetList

    def updateList(self, graph):
        ssc = {}

        for origin in self.adjacencyList:
            vertices = []
            for destination in graph.getEdge(origin):
                vertices.append(destination)
            ssc[origin] = vertices

        self.adjacencyList = ssc

    def getNewList(self):
        return self.adjacencyList

    def getDistance(self, origin, destination):
        return self.distance[origin][destination]

    def addNewEdge(self, origin, destination):
        adList = self.getNewList()
        adList[origin].append(destination)
        self.adjacencyList = adList

    def removeEdge(self, origin, destination):
        adList = self.getNewList()
        adList[origin].remove(destination)
        self.adjacencyList = adList