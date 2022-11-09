import copy

import aisolver.asearch.state
from aisolver.blind.state import *


class WaterSortState(State):
    def __init__(self, tubes, parent=None,  parent_action=None) -> None:
        self.cState = tubes[:]
        super().__init__(parent, parent_action)

    def __eq__(self, state) -> bool:
        if self.get_num_tube() != state.get_num_tube():
            return False
        for i in self.cState:
            flag = False
            for j in state.cState:
                if i == j:
                    flag = True
            if not flag:
                return False
        for i in state.cState:
            flag = False
            for j in self.cState:
                if i == j:
                    flag = True
            if not flag:
                return False
        return True

    def __lt__(self, o: object) -> bool:
        pass

    def get_num_tube(self):
        return len(self.cState)

    def get_tube(self, pos):
        return self.cState[pos]

    def change_tube(self, tube, pos):
        self.cState[pos] = tube

    def set_parent_state(self, parent):
        self.parent = parent

    def get_parent_state(self):
        return self.parent

    def set_parent_action(self, action):
        self.parent_action = action

    def get_parent_action(self):
        return self.parent_action

    def is_goal(self) -> bool:
        """check if all tube in state are qualified. Check if state is target state.

        Returns:
            bool: True if state is target state
        """
        for i in self.cState:
            flag = False
            if i.is_goal():
                flag = True
            if not flag:
                return False
        return True

    def neighbours(self) -> list[State]:
        results = []
        for i in range(self.get_num_tube()):
            for j in range(self.get_num_tube()):
                if i == j:
                    continue
                next_state = self.move((i, j))
                if next_state is not None:
                    flag = False
                    # Check if new state contained in result
                    for it in results:
                        if next_state == it:
                            flag = True
                    if not flag:
                        results.append(next_state)
        return results

    def move(self, action) -> State:
        tube1 = copy.deepcopy(self.get_tube(action[0]))
        tube2 = copy.deepcopy(self.get_tube(action[1]))
        temp = tube1.check_can_poor(tube2)
        if temp[0]:
            state = copy.deepcopy(self)
            tube1.poor_to(tube2, temp[1])
            state.change_tube(tube1, action[0])
            state.change_tube(tube2, action[1])
            state.set_parent_state(self)
            state.set_parent_action(action)
            return state
        return None

    def __str__(self):
        return "|".join('-'.join(str(i) for i in s.get_full_tube()) for s in self.cState)


class ASearchState(WaterSortState, aisolver.asearch.state.ASState):
    def __init__(self, tubes, parent=None, parent_action=None, p_cost=0) -> None:
        """class represent state in watersort game solver using a* algorithm

        Args:
            tubes (list[tube]): list tube contained in state
            parent (State, optional): Previous state of this state. Defaults to None.
            parent_action (tuple(int, int), optional): Action taken by previous state. Defaults to None.
            p_cost (int, optional): Previous cost need to react this state. Defaults to 0.
        """
        super().__init__(tubes, parent, parent_action)
        self.p_cost = p_cost
        self.s_cost = self.get_cost()

    def __lt__(self, state):
        return self.get_p_cost() + self.get_s_cost() < state.get_p_cost() + state.get_s_cost()

    def get_s_cost(self):
        return self.s_cost

    def set_s_cost(self, s_cost):
        self.s_cost = s_cost

    def get_p_cost(self):
        return self.p_cost

    def set_p_cost(self, p_cost):
        self.p_cost = p_cost

    def get_cost(self):
        """state.get_cost: get cost need to go to target state by sum of all tube cost.
        Returns:
            int: cost needed to go to target state
        """
        return sum([i.get_cost() for i in self.cState])

    def move(self, action) -> State:
        state = super().move(action)
        if state is not None:
            state.set_s_cost(state.get_cost())
            state.set_p_cost(self.get_p_cost() + 1)
        return state
