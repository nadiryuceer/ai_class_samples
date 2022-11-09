import queue as Q


class UCS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.put((root.step, root))

    def run(self, target):
        """ YOUR CODE HERE """
        while self.queue.qsize() != 0:
            s = self.queue.get()[1]
            found = self.visited.get(s.UID)
            if not found or (not self.counter):
                self.counter += 1
                if s.is_equal(target): return True, self.counter, s.step
                else:
                    neighbors = self.graph.reveal_neighbors(s)
                    self.addlist(neighbors)
                    self.visited[s.UID] = s

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def addlist(self, adder):
        for i in range(len(adder)):
            self.queue.put((adder[i].step, adder[i]))