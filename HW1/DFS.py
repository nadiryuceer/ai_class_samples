class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.stack = list()
        self.stack.append(root)
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        while len(self.stack) != 0:
            found=self.visited.get(self.stack[0].UID)
            if found:
                self.stack.pop(0)
            else:
                self.counter += 1
                if self.stack[0].is_equal(target):return True, self.counter, self.stack[0].step
                else:
                    self.visited[self.stack[0].UID] = self.stack[0]
                    self.insertelements(self.graph.reveal_neighbors(self.stack.pop(0)))
        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def insertelements(self, neighbors):
        for i in range(len(neighbors)):
            self.stack.insert(i, neighbors[i])