# Bilal Sayed C950 Graph.py

from collections import defaultdict


# graph class to hold packages with weight relations
class Graph:

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    # add node method
    def add_node(self, value):
        self.nodes.add(value)

    # add weighted edge method
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
