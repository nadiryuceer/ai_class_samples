import queue as Q


class AStar:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        self.queue.put((self.manhattan_distance(self.root, target) + self.root.step, self.root))
        while self.queue.qsize() != 0:
            s = self.queue.get()[1]
            found = self.visited.get(s.UID)
            if not found:
                self.counter += 1
                if s.is_equal(target):
                    return True, self.counter, s.step
                else:
                    neighbors = self.graph.reveal_neighbors(s)
                    self.addlist(neighbors, target)
                    self.visited[s.UID] = s

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def manhattan_distance(self, node, end):
        arr = [0] * (self.graph.size + 1)
        brr = [0] * (self.graph.size + 1)
        for i in range(len(node.g_node)):
            for j in range(len(node.g_node[i])):
                arr[node.g_node[i][j]] = [i, j]

        for i in range(len(end.g_node)):
            for j in range(len(end.g_node[i])):
                brr[end.g_node[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0] - brr[i][0]) + abs(arr[i][1] - brr[i][1])
        return dist

    def addlist(self, adder, target):
        for i in range(len(adder)):
            self.queue.put((self.manhattan_distance(adder[i], target)+adder[i].step, adder[i]))