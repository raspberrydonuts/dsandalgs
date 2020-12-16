from collections import defaultdict
class Graph:
    def __init__(self):
        # use defaultdict instead of dict bc when adding edges, if the edge not in graph, 
        # it will not raise error and add it to dict
        # put list in constructor because the values of each key will be a list
        # so this knows to create a default list (empty list) if the key is not in the dictionary
        self.graph = defaultdict(list)

    # adds vertex v as an adjacent node to vertex u
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        queue = []
        visited = []
        queue.append(s)
        visited.append(s)

        while queue:
            v = queue.pop(0)
            print(v, end=" ")
            for adjacent in self.graph[v]:
                if adjacent not in visited:
                    queue.append(adjacent)
                    visited.append(adjacent)
        print("\n")
    
    def DFS(self, s):
        stack = []
        visited = []
        stack.append(s)
        visited.append(s)

        while stack:
            v = stack.pop()
            print(v, end=" ")
            # i reverse it so it goes down left side first
            self.graph[v].reverse()
            for adjacent in self.graph[v]:
                if adjacent not in visited:
                    stack.append(adjacent)
                    visited.append(adjacent)
        print("\n")

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print ("Following is Breadth First Traversal"
                    " (starting from vertex 2)")
    g.BFS(2)

    g2 = Graph()
    g2.addEdge(4, 2)
    g2.addEdge(4, 6)
    g2.addEdge(2, 1)
    g2.addEdge(2, 3)
    g2.addEdge(6, 5)
    g2.addEdge(6, 7)
    g2.BFS(4)
    g2.DFS(4)

    g3 = Graph()
    g3.addEdge(4, 6)
    g3.addEdge(4, 2)
    g3.addEdge(2, 3)
    g3.addEdge(2, 1)
    g3.addEdge(6, 7)
    g3.addEdge(6, 5)
    g3.BFS(4)
    g3.DFS(4)

    # I'm noticing that the order of inserting the edges matters
    # But technically they are still a BFS or DFS, you can sort the list and/or reverse it to try to go in a direction you want
        
