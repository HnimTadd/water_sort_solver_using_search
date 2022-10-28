# from ast import Try
# from sqlite3 import complete_statement
# from time import sleep
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
        print("Init:")
        states[0].print_state()
        for i in range(len(states) - 1):
            print("")
            # print(actions[i])
            print("Poor from {} to {}".format(
                actions[i][0]+1, actions[i][1]+1))

            states[i+1].print_state()
        # for action in actions:
        #     print(action)
        return

    def solve(self, frontier):
        # frontier = StackFrontier()
        start_state = self.init_state.get_copy()
        if start_state.is_finish():
            return True, (start_state, None)
        frontier.add(start_state)
        explored = SetFrontier()
        while not frontier.empty():
            # print()
            # print("exploring: ")
            # print("popped, current length: {}".format(frontier.length()))
            c_state = frontier.pop()
            # c_state.print_state()
            # if c_state.get_parent_state() is not None:
            #     print("parent state")
            #     c_state.get_parent_state().print_state()
            #     if c_state.get_parent_action() is not None:
            #         print("Poor from {} to {}".format(c_state.get_parent_action()[0],c_state.get_parent_action()[1]))
            explored.add(c_state)
            # print("Total explored state: {}".format(explored.length()))
            # if c_state.is_finish():
            #     # continue
            #     print("finish")
            #     states, actions = self.get_solution(c_state)
            #     solutions = (states, actions)
            #     print("Total state: {}".format(explored.length()))
            #     return True, solutions
            avail_move = c_state.avail_next_state()
            for n_state, action in avail_move:
                if frontier.contain(n_state) or explored.contain(n_state):
                    continue
                # print("find new State")
                n_state.set_parent_state(c_state)
                n_state.set_parent_action((action[0], action[1]))
                # print("action: ", action[0],action[1])
                if n_state.is_finish():
                    # continue
                    # print("finish")
                    states, actions = self.get_solution(n_state)
                    solutions = (states, actions)
                    # print("Total state: {}".format(explored.length()))
                    return True, solutions
                # n_state.print_state()
                frontier.add(n_state)
                # print("added, current length: {}".format(explored.length()))
                # print("added state")
                # state.print_state()
        # print("Total state: {}".format(explored.length()))
        return False, None

    def a_search(self):
        frontier = SortedFrontier()
        start_state = self.init_state.get_copy()
        start_state.set_parent_cost(0)
        start_state.set_s_cost(start_state.get_cost())
        frontier.add(start_state)
        # explored = SetFrontier()
        explored = 0
        while not frontier.empty():
            # print('Exploring')
            c_state, _ = frontier.pop()
            # c_state.printState()
            # sleep(0.5)
            explored += 1
            # print("current state: {}".format(explored))
            if c_state.is_finish():
                print("Finish")
                states, actions = self.get_solution(c_state)
                solutions = (states, actions)
                print("Total state: {}".format(explored))
                return True, solutions
            avail_move = c_state.avail_next_state()
            for state, action in avail_move:
                state.set_parent_state(c_state)
                state.set_parent_action(action)
                state.set_parent_cost(c_state.get_p_cost() + 1)
                state.set_s_cost(state.get_cost())
                frontier.add(state)
        print("Total state: {}".format(explored))
        return False, None
