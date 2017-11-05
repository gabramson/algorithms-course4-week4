import Graph

class TwoSATClassifier:
    def __init__(self, variables, clauses):
        self.variables = variables
        self.clauses = clauses
        self.graph = Graph.Graph(2*variables)

    def add_clause(self, first, second):
        if first > 0 and second > 0:
            self.graph.add_edge(first + self.variables - 1, second - 1)
            self.graph.add_edge(second + self.variables - 1, first  - 1)            
        if first > 0 and second < 0:
            self.graph.add_edge(first + self.variables - 1, -1 * second + self.variables - 1)
            self.graph.add_edge(-1 * second - 1, first - 1)
        if first < 0 and second > 0:
            self.graph.add_edge(-1 * first - 1, second  - 1)
            self.graph.add_edge(second * self.variables - 1, -1 * first + self.variables - 1)
        if first < 0 and second < 0:
            self.graph.add_edge(-1 * first - 1, -1 * second + self.variables - 1)
            self.graph.add_edge(-1 * second - 1, -1 * first + self.variables - 1)

    def is_satisfiable(self):
        self.graph.make_scc()
        for scc in self.graph.scc:
            for vertex in scc:
                if vertex < self.variables and vertex + self.variables in scc:
                    return False
        return True