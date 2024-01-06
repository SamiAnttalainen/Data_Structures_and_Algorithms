# Graph class that contains methods for adding and removing nodes and edges, and finding the number of subgraphs in the graph.
class Graph:

    # Initialization
    def __init__(self, n):

        # Initializes the graph
        self.edges = [[] for i in range(n + 1)]

        # Size of the graph
        self.vertexes = n
        

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

        if a > self.vertexes or b > self.vertexes or a < 0 or b < 0:
            return

        if b not in self.edges[a]:
            return
        
        if a not in self.edges[b]:
            return

        self.edges[a].remove(b)
        self.edges[b].remove(a)


    # Method that finds the number of subgraphs in the graph
    def subgraphs(self):
        
        # Checks if the graph is empty
        if self.vertexes == 0:
            return 0

        total = 0
        marked = set()

        # Loops marked list and checks if the vertex is not in the marked list and adds it to the marked list and adds 1 to total.
        for vertex in range(len(self.edges)):

            # Checks if the vertex is not in the marked list
            if vertex not in marked:
                self.marked(vertex, marked)
                total = total + 1

        # Fix for the total size
        total -= 1
        return total


    # Method checks in depth-first order if the vertex is in the marked list and if not, adds it to the marked list.
    def marked(self, vertex, marked):

        # Adds the vertex to the marked list
        marked.add(vertex)

        for next_vertex in self.edges[vertex]:

            # Checks if the next_vertex is not in the marked list
            if next_vertex not in marked:
                self.marked(next_vertex, marked)



if __name__ == "__main__":

    graph = Graph(6)
    edges = ((0, 4), (2, 1),
             (2, 5), (3, 0),
             (5, 1))
    for u, v in edges:
        graph.add(u, v)
    
    print(graph.subgraphs())  # 2
    
    more_connections = ((0, 2), (2, 3),
                        (3, 5), (4, 5))
    for u, v in more_connections:
        graph.add(u, v)

    print(graph.subgraphs())  # 1


