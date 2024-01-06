# Graph class that contains methods for adding and removing nodes and edges, and printing the graph in depth-first and breadth-first order.
class Graph:

    # Initialization
    def __init__(self, n):
        self.vertexes = n
        self.edges = [[] for i in range(n + 1)]

    # Method adds nodes and an edge between them
    def add(self, a, b):

        if a > self.vertexes or b > self.vertexes or a < 0 or b < 0:
            return
        
        if b in self.edges[a]:
            return
        
        if a in self.edges[b]:
            return

        self.edges[a].append(b)
        self.edges[b].append(a)

    # Method remove the edge between two nodes if there is one, else does nothing.
    def remove(self, a, b):

        if b not in self.edges[a]:
            return
        
        if a not in self.edges[b]:
            return

        self.edges[a].remove(b)
        self.edges[b].remove(a)


    # Method prints the graph in depth-first order
    def dft(self, start_vertex):

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

    

if __name__ == "__main__":
    graph = Graph(8)

    edges = ((0, 2), (0, 4), (2, 1),
             (2, 3), (2, 5), (3, 0),
             (3, 5), (4, 5), (5, 1))
    for u, v in edges:
        graph.add(u, v)

    graph.dft(0)
    graph.bft(0)

    graph.remove(0, 2)
    graph.remove(2, 5)
    graph.remove(1, 4)

    graph.dft(0)
    graph.bft(0)
  
