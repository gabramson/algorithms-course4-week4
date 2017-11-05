import collections

class Graph:
    def __init__(self, vertices):
        self.scc = []
        self.vertices = vertices
        self.forward = [set() for _ in range(vertices)]
        self.reverse = [set() for _ in range(vertices)]
        self.traverse_order = collections.deque()
        self.visited = [False for _ in range(self.vertices)]
        self.current_scc = 0
        
    def add_edge(self, head, tail):
        self.forward[head].add(tail)
        self.reverse[tail].add(head)

    def make_scc(self):
        for vertex in range(self.vertices):
            if not self.visited[vertex]:
                self.__fill_order(vertex)
        self.visited = [False for _ in range(self.vertices)]
        self.scc.append(set())
        for vertex in self.traverse_order:
            if not self.visited[vertex]:
                self.__DFS(vertex)
                self.current_scc += 1
                self.scc.append(set())

    def __fill_order(self, vertex):
        self.visited[vertex] = True
        for next_vertex in self.forward[vertex]:
            if not self.visited[next_vertex]:
                self.__fill_order(next_vertex)
        self.traverse_order.appendleft(vertex)

    def __DFS(self, vertex):
        self.visited[vertex] = True
        self.scc[self.current_scc].add(vertex)
        for next_vertex in self.reverse[vertex]:
            if not self.visited[next_vertex]:
                self.__DFS(next_vertex)