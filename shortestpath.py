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
        # self.edges[a].append((c, b))
        # self.edges[c].append((a, b))
        # self.edges[b].append((c, a))
        # self.edges[c].append((b, a))


    # Method remove the edge between two nodes if there is one, else does nothing.
    def remove(self, a, b):
        self.edges[a] = [edge for edge in self.edges[a] if edge[0] != b]
        self.edges[b] = [edge for edge in self.edges[b] if edge[0] != a]

        # self.edges[a] = [vertex for vertex in self.edges[a] if vertex != b]
        # self.edges[b] = [vertex for vertex in self.edges[b] if vertex != a]


    # Method prints the graph in depth-first order
    def dft(self, start_vertex):

        # Checks if the start_vertex is valid
        if start_vertex > self.vertexes or start_vertex < 0:
            return

        # List that contains the visited nodes
        visited = set()

        # Stack that contains the nodes that are to be visited
        stack = [start_vertex]

        while stack:

            # Pops the last item from the stack
            node = stack.pop()

            # If the node has not been visited, then print it and add it to the visited list
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                stack.extend(sorted((vertex for vertex in self.edges[node] if vertex not in visited), reverse=True))

        print()

    # Method prints the graph in breadth-first order
    def bft(self, start_vertex):

        # Checks if the start_vertex is valid
        if start_vertex > self.vertexes or start_vertex < 0:
            return


        # List that contains the visited vertexes
        visited = set()

        # Stack that contains the nodes that are to be visited
        stack = [start_vertex]

        while stack:

            # Pops the first item from the stack
            node = stack.pop(0)

            # If the node has not been visited, then print it and add it to the visited list
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                stack.extend(sorted(vertex for vertex in self.edges[node] if vertex not in visited))
        print()


    def shortest_path(self, start_vertex, end_vertex):
        if start_vertex > self.vertexes or start_vertex < 0:
            return
        if end_vertex > self.vertexes or end_vertex < 0:
            return

        # visited = set()
        distances = [float('inf')] * (self.vertexes + 1)
        distances[start_vertex] = 0
        previous_vertices = [None] * (self.vertexes + 1)
        unvisited_vertices = list(range(self.vertexes + 1))

        while unvisited_vertices:
            current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])
            unvisited_vertices.remove(current_vertex)

            if distances[current_vertex] == float('inf'):
                break

            for neighbor, weight in self.edges[current_vertex]:
                distance = distances[current_vertex] + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex

        # Reconstruct and print the path
        path = []
        current = end_vertex
        while current is not None:
            path.insert(0, current)
            current = previous_vertices[current]

        for vertex in path:
            print(vertex, end=' ')
        print()

        return distances[end_vertex]

    # def shortest_path(self, start_vertex, end_vertex):
    #     if start_vertex > self.vertexes or start_vertex < 0:
    #         return
    #     if end_vertex > self.vertexes or end_vertex < 0:
    #         return

    #     distances = [float('inf')] * (self.vertexes + 1)
    #     distances[start_vertex] = 0
    #     previous_vertices = [None] * (self.vertexes + 1)
    #     unvisited_vertices = list(range(1, self.vertexes + 1))

    #     while unvisited_vertices:
    #         current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])
    #         unvisited_vertices.remove(current_vertex)

    #         if distances[current_vertex] == float('inf'):
    #             break

    #         for neighbor in self.edges[current_vertex]:
    #             distance = distances[current_vertex] + 1  # Assume unit weight for simplicity

    #             if distance < distances[neighbor]:
    #                 distances[neighbor] = distance
    #                 previous_vertices[neighbor] = current_vertex

    #     # Reconstruct and print the path
    #     path = []
    #     current = end_vertex
    #     while current is not None:
    #         path.insert(0, current)
    #         current = previous_vertices[current]

    #     print("Shortest path:", path)
    #     return distances[end_vertex]


if __name__ == "__main__":

    graph = Graph(6)

    connections = ((0, 1, 24), (0, 2, 13),
                (1, 5,  9), (2, 5, 19),
                (3, 0, 25), (4, 0, 20),
                (5, 3, 18), (5, 4, 36))

    for u, v, w in connections:
        graph.add(u, v, w)

    graph.shortest_path(0, 3) # 0 2 5 3
    graph.shortest_path(3, 1) # 3 0 1
    graph.shortest_path(2, 4) # 2 5 4

    graph.remove(0, 2)
    graph.remove(3, 0)

    graph.shortest_path(0, 3) # 0 1 5 3
    graph.shortest_path(3, 1) # -1
    graph.shortest_path(2, 4) # 2 5 4

    # graph = Graph(10)
    # edges = ((0, 1, 25), (0, 2,  6), (1, 3, 10),
    #          (1, 4,  3), (2, 3,  7), (2, 5, 25),
    #          (3, 4, 12), (3, 5, 15), (3, 6,  4),
    #          (3, 7, 15), (3, 8, 20), (4, 7,  2),
    #          (5, 8,  2), (6, 7,  8), (6, 8, 13),
    #          (6, 9, 15), (7, 9,  5), (8, 9,  1))
    # for u, v, w in edges:
    #     graph.add(u, v, w)

    # graph.shortest_path(0, 9)   # 0 2 3 6 7 9
    # graph.remove(3, 6)
    # graph.remove(5, 6)
    # graph.shortest_path(0, 9)   # 0 2 3 5 8 9