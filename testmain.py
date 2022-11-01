import sys
from object.tube import Tube
from object.state import State
from solver import *
import xml.etree.ElementTree as Et

tree = Et.parse("E:\\Project\\nmai\waterpuzzle\\input\\levels.xml")
root = tree.getroot()
# print(len(sys.argv))
if len(sys.argv) == 2:
    level = [i for i in range(1, 41)]
    method = sys.argv[1].upper()
elif len(sys.argv) == 3:
    level = [sys.argv[1]]
    method = sys.argv[2].upper()
else:
    # level =[5]
    # level = [i for i in range(1, 41)]
    level = [6]
    method = "as"
    # print("error")
    # exit()


def get_input(lv):
    print("Level = {}".format(lv))
    y = ".//*[@id='{}']".format(lv)
    x = root.findall(y)[0]
    tube = [list(map(int, t.text.split('_').__reversed__()))
            for t in x.iter('glass')]
    for i in tube:
        # print(i)
        while len(i) != 0 and i[-1] == 0:
            i.pop(-1)
        # print(i)
    n = 4
    tubes = [Tube(i, n) for i in tube]
    state = State(tubes)
    return state


def main(levels):
    for LEVEL in levels:
        init_state = get_input(LEVEL)
        # init_state.print_state()
        # print("\nCurrent state")
        # init_state.print_state()
        game = Solver(init_state)
        res = []
        solutions = []
        if method == "DFS":
            frontier = StackFrontier()
            res, solutions = game.solve(frontier)
        elif method == "BFS":
            frontier = QueueFrontier()
            res, solutions = game.solve(frontier)
        elif method == "AS":
            res, solutions = game.a_search()
        if res and solutions is not None:
            # game.print_solution(solutions)
            # print("s")
            print(len(solutions[1]))


main(level)
# get_input(1).print_state()
# a = get_input(5)
# b = a.get_copy()
# a.print_state()
# tube3 = a.get_tube(3)
# tube4 = a.get_tube(4)
# a.change_tube(tube4, 3)
# a.change_tube(tube3, 4)
# print()
# a.print_state()
# print(b.equal(a))
# them list day hay chua vao stage => giam so luong so sanh.

# moi stage cos the di theo nhieu huong khac nhau, moi huong deu co the dan den dich
# => dfs loi the hon

# tinh den chuyen mot o co mau o duoi thi cang khac nhau so vowi o tren
