# Graph that has Dijkstra's shortest path algorithm implemented
class Graph:

    # Initialization
    def __init__(self, n):
        self.vertexes = n
        self.edges = [[] for i in range(n + 1)]

    # Method adds nodes and an edge with weight between them
    def add(self, a, b, c):

        if a in self.edges[b]:
            return
        
        if b in self.edges[a]:
            return

        self.edges[a].append((b, c))  # Add edge from a to b with weight c
        self.edges[b].append((a, c))  # Add edge from b to a with weight c



    # Method remove the edge between two nodes if there is one, else does nothing.
    def remove(self, a, b):
        self.edges[a] = [edge for edge in self.edges[a] if edge[0] != b]
        self.edges[b] = [edge for edge in self.edges[b] if edge[0] != a]


    def all_paths(self):

        # List that contains the paths
        paths = []

        # List that contains the visited nodes
        visited = set()

        # Stack that contains the nodes that are to be visited
        stack = [1]

        while stack:

            # Pops the last item from the stack
            node = stack.pop()

            # If the node has not been visited, then add it to the visited list
            if node not in visited:
                visited.add(node)
                stack.extend(sorted((vertex for vertex in self.edges[node] if vertex not in visited), reverse=True))

            # If the node has been visited and the node is the last node, then add the path to the paths list
            if node in visited and node == self.vertexes:
                paths.append(visited.copy())

        return paths
    

if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
             (2, 3, 1), (2, 5, 2), (3, 0, 6),
             (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    M = graph.all_paths()
    for weights in M:
        for weight in weights:
            print(f"{weight:3d}", end="")
        print()
    #  0 12  7  8  9  9
    # -1  0 -1 -1 -1 -1
    #  7  5  0  1 16  2
    #  6  8 13  0 15  2
    # -1  7 -1 -1  0  1
    # -1  6 -1 -1 -1  0