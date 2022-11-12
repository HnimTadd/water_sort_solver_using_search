import argparse
import os
import psutil
import sys
import time
import watersort.watersort as watersort_module


def parse_input():
    parser = argparse.ArgumentParser()
    msg = "Watersort solver"
    parser.add_argument("-l", "--Level", help="Game level: [1,40]", type=int, required=True)
    parser.add_argument("-a", "--Algorithm", help="Algorithm: dfs/bfs/as", type=str, required=True)
    parser.add_argument("-d", "--Demo", help="Demo", type=int, default=1)
    parser.add_argument("-t", "--Type", help="Demo type: step/auto", type=str, default="step")
    parser.add_argument("-s", "--Delay", help="Auto demo delay time: float", type=float, default="0.5")
    args = parser.parse_args()
    return args


def process_input(args):
    result = {"Algorithm": args.Algorithm}
    result.update({"Level": args.Level})
    result.update({"Demo": args.Demo})
    result.update({"Type": args.Type})
    result.update({"Delay": args.Delay})
    return result


def main(input_data):
    algorithm = input_data["Algorithm"].upper()
    level = input_data["Level"]
    solutions = []
    game = watersort_module.WaterSort()
    print("Algorithm: {} \t Input: {}".format(algorithm, level))
    if algorithm in ["DFS", "BFS", "AS"]:
        start = time.time()
        begin_mem = psutil.Process(os.getpid()).memory_info().rss
        solutions = game.solve(level, algorithm)
        end_mem = psutil.Process(os.getpid()).memory_info().rss
        end = time.time()
        print("Memory usage: {:.3f}".format((end_mem - begin_mem) * 1e-6), "MB")
        print("Time to solve: {:.3f}".format(end - start), "second")
        if solutions is not None:
            print("Step to complete: {}".format(len(solutions)))
            input()
            if input_data["Demo"] == 1:
                if input_data["Type"].upper() == "AUTO":
                    demo_type = 0
                else:
                    demo_type = 1
                game.demo(solutions, demo_type, input_data["Delay"])
        else:
            print("Can't solve")
    sys.exit()


if __name__ == '__main__':
    input_parse = process_input(parse_input())
    main(input_parse)
