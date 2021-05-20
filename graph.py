import matplotlib
import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from adjacencyList import AdjacencyList

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=13, height=13, dpi=50, adList=None):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.plot(adList)

    def plot(self, adList):
        self.axes.clear()
        adjacencyList = AdjacencyList()
        G = nx.DiGraph()

        for origin in adList:
            G.add_node(origin)

            for destination in adList[origin]:
                G.add_node(destination)
                G.add_edge(origin, destination, weight=adjacencyList.getDistance(origin, destination))

        edge_labels = dict([((origin, destination), d['weight']) for origin, destination, d in G.edges(data=True)])
        pos = nx.circular_layout(G)

        nx.draw(
            G,
            with_labels=True,
            ax=self.axes,
            node_size=10000,
            pos=pos,
            connectionstyle='arc3, rad=0.15',
            node_color='skyblue',
            node_shape='o',
            alpha=0.5,
            linewidths=4,
            arrows=True,
            font_size=20,
            font_weight='bold',
            arrowsize=60,
            arrowstyle='->',
            width=2,
        )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=self.axes, font_size=20)

        self.fig.set_facecolor('#f0f0f0')

