class Graph:
    scc = []
    
    def __init__(self, vertices):
        self.forward = [set() for _ in range(vertices)]
        self.reverse = [set() for _ in range(vertices)]
        
    def add_edge(self, head, tail):
        self.forward[head].add(tail)
        self.reverse[tail].add(head)

    def make_scc(self):
        x=1