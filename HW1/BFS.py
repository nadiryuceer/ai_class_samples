class BFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = list()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.append(root)

    def run(self, target):
        """ YOUR CODE HERE """
        while len(self.queue) != 0:
            found = self.visited.get(self.queue[0].UID)
            if found and self.counter:
                self.queue.pop(0)
            else:
                self.counter += 1
                if self.queue[0].is_equal(target):
                    return True, self.counter, self.queue[0].step
                else:
                    self.visited[self.queue[0].UID] = self.queue[0]
                    self.queue += self.graph.reveal_neighbors(self.queue.pop(0))

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0
