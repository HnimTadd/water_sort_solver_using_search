from aisolver.blind.solver import *


class ASearch:
    def __init__(self,  frontier, initial_state) -> None:
        self.init_state = initial_state
        self.frontier = frontier

    def solve(self):
        self.frontier.append(self.init_state)
        while not self.frontier.is_empty():
            current_state = self.frontier.pop()
            if current_state.is_goal():
                return Solver.solution(current_state)
            neighbours = current_state.neighbours()
            for next_state in neighbours:
                self.frontier.append(next_state)
        return None
