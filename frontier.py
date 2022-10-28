# from object.state import state


class Frontier:
    def __init__(self) -> None:
        self.frontier = []

    def add(self, node):
        # if not isinstance(node, state):
        #     raise Exception("Not state")
        # else:
        self.frontier.append(node)

    def length(self):
        return len(self.frontier)

    def contain(self, node):
        for state in self.frontier:
            if state.equal(node):
                return True
        return False

    def empty(self):
        return len(self.frontier) == 0

    def pop(self):
        pass


class StackFrontier(Frontier):
    def pop(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(Frontier):
    def pop(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class SetFrontier(Frontier):
    def add(self, node):
        if self.contain(node):
            return
        else:
            self.frontier.append(node)
            return

    def pop(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class SortedFrontier(StackFrontier):
    def __init__(self) -> None:
        super().__init__()

    def get_node_pos(self, node):
        for i in range(len(self.frontier)):
            if self.frontier[i][0].equal(node):
                return i
        return -1

    def remove(self, pos):
        if pos < 0 or pos >= len(self.frontier):
            raise Exception("Out of range")
        else:
            self.frontier = self.frontier[:pos] + self.frontier[pos + 1:]

    def add(self, node):
        s_cost = node.get_s_cost() + node.get_p_cost()
        if self.contain(node):
            self.remove(self.get_node_pos(node))
        for i in range(len(self.frontier)):
            if self.frontier[i][1] < s_cost:
                self.frontier.insert(i, [node, s_cost])
                return
        self.frontier.append([node, s_cost])

    def contain(self, node):
        for ITER in self.frontier:
            if ITER[0].equal(node):
                return True
        return False
