import xml.etree.ElementTree as Et
import aisolver.blind.frontier as fr
import aisolver.blind.solver as blind_solver
import aisolver.asearch.solver as a_solver
import watersort.state as watersort_state
from watersort.tube import *
from termcolor import colored
import os
import time

Color = {
    '0': "  ",
    '1': colored("██", "magenta"),
    '2': colored("██", "blue"),
    '3': colored("██", "red"),
    '4': colored("██", "green"),
    '5': colored("██", "cyan"),
    '6': colored("██", "yellow"),
    '7': colored("██", "grey")
}


def clear_scr():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_frame(input_data: watersort_state.WaterSortState):
    x = ""
    tubes = []
    for i in range(input_data.get_num_tube()):
        tubes.append(input_data.get_tube(i).get_full_tube())
    for i in range(len(tubes[0])).__reversed__():
        for j in range(len(tubes)):
            x += "|" + Color[str(tubes[j][i])] + "|" + "  "
        x += "\n"
    for i in range(len(tubes)):
        x += " {} ".format(i + 1) + "   "
    return x


class WatersortDemo:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def demo_by_step(self, actions):
        n_state = self.initial_state
        step = 0
        i = 0
        while 0 <= i < len(actions):
            clear_scr()
            print(get_frame(n_state))
            print("Step {}: Pour from {} to {} \n".format(
                step, actions[i][0] + 1, actions[i][1] + 1))
            step += 1
            x = str(input("Press N: Next, P:Previous, Q:Quit "))
            if x.upper() == "N" or x.upper() == "":
                n_state = n_state.move(actions[i])
                i += 1
            elif x.upper() == "P":
                if i == 0:
                    print("At init stage, press q to quit")
                    continue
                else:
                    n_state = n_state.get_parent_state()
                    i -= 1
            elif x.upper() == "Q":
                break
        clear_scr()
        print(get_frame(n_state))
        if i == len(actions):
            print("Done in {} steps".format(step))

    def demo(self, actions, delays):
        n_state = self.initial_state
        step = 0
        for action in actions:
            clear_scr()
            print(get_frame(n_state))
            n_state = n_state.move(action)
            step += 1
            print("Step {}: Pour from {} to {} \n".format(
                step, action[0] + 1, action[1] + 1))
            time.sleep(delays)
            clear_scr()
        print(get_frame(n_state))
        print("Done in {} steps".format(step))


class WaterSort:
    def __init__(self):
        self.initial_state = None
        tree = Et.parse("watersort/input.xml")
        self.root = tree.getroot()

    def get_input(self, lv, state_type):
        print("Level = {}".format(lv))
        y = ".//*[@id='{}']".format(lv)
        x = self.root.findall(y)[0]
        tube = [list(map(int, t.text.split('_').__reversed__()))
                for t in x.iter('glass')]
        for i in tube:
            # print(i)
            while len(i) != 0 and i[-1] == 0:
                i.pop(-1)
            # print(i)
        n = 4
        tubes = [Tube(i, n) for i in tube]
        if state_type.upper() == "BLIND":
            state = watersort_state.WaterSortState(tubes)
        elif state_type.upper() == "AS":
            state = watersort_state.ASearchState(tubes)
        return state

    def solve(self, level, algorithm):
        if algorithm.upper() == "DFS":
            frontier = fr.StackFrontier()
            self.initial_state = self.get_input(level, "BLIND")
            solver = blind_solver.Solver(frontier, self.initial_state)
        elif algorithm.upper() == "BFS":
            frontier = fr.QueueFrontier()
            self.initial_state = self.get_input(level, "BLIND")
            solver = blind_solver.Solver(frontier, self.initial_state)
        elif algorithm.upper() == "AS":
            frontier = fr.PriorityQueueFrontier()
            self.initial_state = self.get_input(level, "AS")
            solver = a_solver.ASearch(frontier, self.initial_state)
        if solver is not None:
            solutions = solver.solve()
            if solutions is not None:
                return solutions
            else:
                print("Can't solve")
                return None
        else:
            print("Invalid input")
            return None

    def demo(self, action, by_step, delay=0.5):
        demo = WatersortDemo(self.initial_state)
        if by_step:
            demo.demo_by_step(action)
        else:
            demo.demo(action, delay)
        return

