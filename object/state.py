# from tube import tube
class State:
    # tubes: list tube
    def __init__(self, tubes, p_state=None, p_action=None, p_cost=None, s_cost=None):
        self.cState = tubes[:]
        # self.nTubes = tubes[:]
        self.pState = p_state
        self.pAction = p_action
        self.pCost = p_cost
        self.sCost = s_cost
        # self.sCost = sCost

    def print_state(self):
        for i in self.cState:
            i.print_tube()
        if self.pCost is not None:
            print("Current p cost:", self.pCost)
            print("Current cost: ", self.pCost + self.get_cost())
        else:
            # print("Current p Cost: 0")
            if self.pCost is not None and self.get_cost() is not None:
                print("Current cost: ", self.pCost +  # type: ignore
                      self.get_cost())  # type: ignore

    def get_p_cost(self):
        return self.pCost

    def set_parent_cost(self, cost):
        self.pCost = cost

    def set_s_cost(self, cost):
        self.sCost = cost

    def get_s_cost(self):
        return self.sCost

    def get_num_tube(self):
        return len(self.cState)

    def is_finish(self):
        # return len(self.nTubes) == 0
        for i in self.cState:
            if not i.is_finish():
                return False
        return True

    # def is_finish(self):
    #     for i in self.cState:
    #         if i.get_current_volume() == 0:
    #             continue
    #         if i.get_cost() == -6:
    #             continue
    #         return False
    #     return True

    def get_cost(self):
        # return -4
        return sum([i.get_cost() for i in self.cState])

    def change_tube(self, new_tube, pos):
        self.cState[pos] = new_tube.get_copy()

    def get_tube(self, pos):
        return self.cState[pos].get_copy()

    # def __eq__(self, other):
    #     if self.get_num_tube() != state.get_num_tube():
    #         return False
    #     for i in self.cState:
    #         flag = False
    #         for j in state.cState:
    #             if i.equal(j):
    #                 flag = True
    #         if not flag:
    #             return False
    #     for i in state.cState:
    #         flag = False
    #         for j in self.cState:
    #             if i.equal(j):
    #                 flag = True
    #         if not flag:
    #             return False
    #     return True

    def equal(self, state):
        if self.get_num_tube() != state.get_num_tube():
            return False
        for i in self.cState:
            flag = False
            for j in state.cState:
                if i.equal(j):
                    flag = True
            if not flag:
                return False
        for i in state.cState:
            flag = False
            for j in self.cState:
                if i.equal(j):
                    flag = True
            if not flag:
                return False
        return True

    def set_parent_state(self, p_state):
        self.pState = p_state

    def get_parent_state(self):
        return self.pState

    def get_parent_action(self):
        return self.pAction

    def set_parent_action(self, p_action):
        self.pAction = p_action

    def get_copy(self):
        return State(self.cState[:], )

    # def get_d_cost(self, list):
    #     return list[0].get_cost() - self.get_cost()

    # return all avail state this state can reach if do the action
    def avail_next_state(self):
        results = []
        for i in range(self.get_num_tube()):
            for j in range(self.get_num_tube()):
                if i == j:
                    continue
                current_state = self.get_copy()
                tube1 = current_state.get_tube(i).get_copy()
                tube2 = current_state.get_tube(j).get_copy()
                temp = tube1.poor_to(tube2)
                if temp:
                    current_state.change_tube(tube1, i)
                    current_state.change_tube(tube2, j)
                    flag = False
                    for it in results:
                        if current_state.equal(it[0]):
                            flag = True
                    if not flag:
                        results.append([current_state, (i, j)])
        return results

    def __str__(self):
        return "||||".join('-'.join(str(i) for i in s.get_full_tube()) for s in self.cState)
