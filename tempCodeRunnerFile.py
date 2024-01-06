    def dfs(self, vertex, visited, subgraph):
        visited.add(vertex)
        subgraph.append(vertex)

        for neighbor in self.edges[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, subgraph)