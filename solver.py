from frontier import *


class Solver:
    def __init__(self, input_data):
        self.init_state = input_data

    @staticmethod
    def get_solution(state):
        if state is None:
            return [], []
        actions = []
        track_state = []
        while state.pState is not None:
            actions.append(state.get_parent_action())
            track_state.append(state)
            state = state.get_parent_state()
        track_state.append(state)
        actions.reverse()
        track_state.reverse()
        solution = (track_state, actions)
        return solution

    @staticmethod
    def print_solution(solutions):
        states, actions = solutions
        if len(states) == 1 or len(actions) == 0:
            return
        # print("Init:")
        # states[0].print_state()
        for i in range(len(states) - 1):
            print("")
            print("Poor from {} to {}".format(
                actions[i][0]+1, actions[i][1]+1))
            # states[i+1].print_state()
        return

    def solve(self, frontier):
        # frontier = StackFrontier()
        start_state = self.init_state.get_copy()
        if start_state.is_finish():
            return True, (start_state, None)
        frontier.add(start_state)
        explored = SetFrontier()
        e_c = 0
        while not frontier.empty():
            c_state = frontier.pop()
            explored.add(c_state)
            e_c += 1
            avail_move = c_state.avail_next_state()
            for n_state, action in avail_move:
                if frontier.contain(n_state) or explored.contain(n_state):
                    continue
                n_state.set_parent_state(c_state)
                n_state.set_parent_action((action[0], action[1]))
                if n_state.is_finish():
                    states, actions = self.get_solution(n_state)
                    solutions = (states, actions)
                    print("Total state explored: {}".format(e_c))
                    return True, solutions
                frontier.add(n_state)
        return False, None

    def a_search(self):
        frontier = SortedFrontier()
        start_state = self.init_state.get_copy()
        start_state.set_parent_cost(0)
        start_state.set_s_cost(start_state.get_cost())
        frontier.add(start_state)
        explored = 0
        while not frontier.empty():
            c_state, _ = frontier.pop()
            explored += 1
            avail_move = c_state.avail_next_state()
            for n_state, action in avail_move:
                n_state.set_parent_state(c_state)
                n_state.set_parent_action(action)
                n_state.set_parent_cost(c_state.get_p_cost() + 1)
                n_state.set_s_cost(n_state.get_cost())
                if n_state.is_finish():
                    print("Finish")
                    states, actions = self.get_solution(n_state)
                    solutions = (states, actions)
                    print("Total state: {}".format(explored))
                    return True, solutions
                frontier.add(n_state)
        print("Total state: {}".format(explored))
        return False, None
