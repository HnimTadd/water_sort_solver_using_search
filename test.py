from object.tube import Tube
from object.state import State
from solver import *
# from bs4 import BeautifulSoup
# import treebuilder as tb
import xml.etree.ElementTree as Et
from threading import Thread
import threading
from testmain import *

# import json
# # with open("input/levels.xml") as f:
# #     print(f.read())
# #     data = tb.TreeBuilder(f.read())
# #     for i in data['level']:
# #         print(i)
# tree = et.parse('input/levels.xml')
# root = tree.getroot()
# # for c in root:
# #     print(c.tag, c.attrib)
# print(root.attrib)
# y = ".//*[@id='{}']".format(4)
# x = root.findall(y)[0]
# tube = [list(map(int, t.text.split('_').__reversed__())) for t in x.iter('glass')]
# for i in tube:
#     for j in i:
#         while len(i) != 0 and j == 0:
#             i.pop()
# # print(tube)
# n = 4
# tubes = [Tube(i, n) for i in tube]
# state = State(tubes)
# state.print_state()
# init_state = state.get_copy()
# tree.findall('''.//*[@id='fooID']''')[0]
# for j in root.iter('level'):
#     print("current level: ", j.attrib)
#     for t in j.iter('glass'):
#         print(t.text)
# bs_data = BeautifulSoup(data, 'xml')
# b_game = bs_data.find_all('game')
# print(b_game)
# color = {'xd': 1, 'h': 2, 'c': 3, 'xl': 4, 'd': 5, 'x': 6, 'v': 7}
# tube1 = Tube([color[i] for i in ('c', 'c', 'd', 'xd')], 4)
# tube2 = Tube([color[i] for i in ('xd', 'c', 'd', 'xd')], 4)
# tube3 = Tube([color[i] for i in ('d', 'xd', 'c', 'd')], 4)
# tube4 = Tube([color[i] for i in (())], 4)
# tube5 = Tube([color[i] for i in (())], 4)
#
# init_state = State([tube1, tube2, tube3, tube4,
#                     tube5])
#
# scnd_state = init_state.get_copy()
#
# for levell in range(1):
#     level = 16
#     print()
#     print("Level = {}".format(level))
#     y = ".//*[@id='{}']".format(level)
#     x = root.findall(y)[0]
#     tube = [list(map(int, t.text.split('_').__reversed__()))
#             for t in x.iter('glass')]
#     for i in tube:
#         for j in i:
#             while len(i) != 0 and j == 0:
#                 i.pop()
#     # print(tube)
#     n = 4
#     tubes = [Tube(i, n) for i in tube]
#     state = State(tubes)
#     # state.print_state()
#     init_state = state.get_copy()
#     game = Solver(init_state)
#     res, solutionss = game.solve()
#     if res and solutionss is not None:
#         # game.print_solution(solutions=solutions)
# print(len(solutionss[1]))
# res1, solutions = game.a_search()
# if res1 and solutions is not None:
#     print(len(solutions[1]))
# game.print_solution(solutions)

# tube1 = Tube([7, 1, 1, 1], 4)
# # print(tube1.get_cost())
# tube2 = Tube([7, 3, 1], 4)
# tube3 = Tube([1, 1, 1, 1], 4)
# print(tube3.get_cost())
# tube4 = Tube([1, 1, 1, 1], 4)
# tube5 = Tube([2, 2, 2, 2], 4)
# tube6 = Tube([3, 3, 3, 3], 4)
# tube7 = Tube([], 4)
# tube8 = Tube([4, 4, 4, 4], 4)
# tube9 = Tube([5, 5, 5, 5], 4)
# state = State([tube3, tube4, tube5, tube6, tube7, tube8, tube9])
# for j in state.cState:
# #     print(j.get_cost())
# print(state.is_finish())
# # for i in state.nTubes:
# #     i.print_tube()
# # tube1.poor_to(tube2)
# # print()
# # state.nTubes.pop(1)
# # for i in state.cState:
# #     i.print_tube()
# # tube1.print_info()
# # tube2.print_info()
# # x = tube1.poor_to(tube2)
# # print(x)
# # tube1.print_tube()
# tube2.print_tube()

tree = Et.parse("E:\\Project\\nmai\\waterpuzzle\\input\\levels.xml")
root = tree.getroot()
thread = []
for i in range(1, 41):
    thread.append(threading.Thread(name=main([i])))
for i in range(1, 41):
    thread[i].start()
    print("Done level {}".format(i))
