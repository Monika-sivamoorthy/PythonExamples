"""
What is topological sort?
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that
for every directed edge u->v, vertex u comes before v in the ordering.

Note:
1. Topological sorting can be applied only to Directed Acyclic Graph
2. Every DAG will have atleast one topological ordering
"""


class Graph:
    def __init__(self, *vertices):
        self.vertices = vertices
        self.adjacency_map = {v: [] for v in vertices}

    def add_edge(self, u, v):
        self.adjacency_map[u].append(v)

    def print_adjacency_matrix(self):
        vertices_count = len(self.vertices)
        matrix = [[0 for _ in range(vertices_count)] for _ in range(vertices_count)]
        for vertex in self.vertices:
            for neighbour in self.adjacency_map[vertex]:
                matrix[vertex][neighbour] = 1
        for row in matrix:
            print(row)


class TopologicalSorting:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.stack = []

    def dfs(self, vertex):
        if vertex not in self.visited:
            self.visited.append(vertex)
            for neighbour in self.graph.adjacency_map[vertex]:
                self.dfs(neighbour)
            self.stack.insert(0, vertex)

    def topological_sort(self):
        for vertex in self.graph.vertices:
            if vertex not in self.visited:
                self.dfs(vertex)
        return self.stack


if __name__ == "__main__":
    grph = Graph(5, 4, 3, 2, 1, 0)
    grph.add_edge(5, 2)
    grph.add_edge(5, 0)
    grph.add_edge(4, 0)
    grph.add_edge(4, 1)
    grph.add_edge(2, 3)
    grph.add_edge(3, 1)
    print("\nAdjacency matrix:")
    print("----------------------------------------------------------------------")
    grph.print_adjacency_matrix()

    print("\nAdjacency list:")
    print("----------------------------------------------------------------------")
    print(grph.adjacency_map)

    sort_obj = TopologicalSorting(grph)
    print(f"\nTopological sorting:")
    print("----------------------------------------------------------------------")
    print(f"{sort_obj.topological_sort()}")

# OUTPUT:
# ===========================================
#
# Adjacency matrix:
# ----------------------------------------------------------------------
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 1, 0, 0]
# [0, 1, 0, 0, 0, 0]
# [1, 1, 0, 0, 0, 0]
# [1, 0, 1, 0, 0, 0]
#
# Adjacency list:
# ----------------------------------------------------------------------
# {5: [2, 0], 4: [0, 1], 3: [1], 2: [3], 1: [], 0: []}
#
# Topological sorting:
# ----------------------------------------------------------------------
# [4, 5, 0, 2, 3, 1]
#

