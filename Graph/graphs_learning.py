class Graph:
    def __init__(self):
        self.adjacency_list = {}  # Use a dictionary, not a list

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []  # Initialize an empty adjacency list

    def add_edge(self, vertex1, vertex2, bidirectional=True):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            if bidirectional:  # If undirected graph, add edge in both directions
                self.adjacency_list[vertex2].append(vertex1)

    def display(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex} -> {neighbors}")

# Example Usage:
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')

g.display()
