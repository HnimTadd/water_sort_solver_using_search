from aisolver.blind.state import State


class Frontier:

    frontier: list[State]

    def __init__(self):
        self.frontier = []

    def is_empty(self):
        if len(self.frontier) == 0:
            return True
        return False

    def contains(self, item):
        for index, state in enumerate(self.frontier):
            if state == item:
                return True
        return False

    def append(self, state):
        if not isinstance(state, State):
            print(f"Cannot append {State} to frontier")
        else:
            self.frontier.append(state)

    def pop(self):
        pass

    def __str__(self) -> str:
        frontier_string = "Frontier: \n"
        for state in self.frontier:
            frontier_string += f"\t{str(state)}"

        return frontier_string


class StackFrontier(Frontier):
    def pop(self):
        return self.frontier.pop()


class QueueFrontier(Frontier):
    def pop(self):
        return self.frontier.pop(0)


class PriorityQueueFrontier(StackFrontier):
    def get_node_pos(self, state):
        for i in range(len(self.frontier)):
            if self.frontier[i] == state:
                return i
        return -1

    def remove(self, pos):
        if pos < 0 or pos >= len(self.frontier):
            raise Exception("Out of index")
        else:
            self.frontier = self.frontier[:pos] + self.frontier[pos+1:]

    def append(self, state):
        x = self.get_node_pos(state)
        if x != -1:
            if self.frontier[x] > state:
                self.remove(x)
        index = 0
        for i in self.frontier:
            if i < state:
                self.frontier.insert(index, state)
                return
            index += 1
        self.frontier.append(state)
