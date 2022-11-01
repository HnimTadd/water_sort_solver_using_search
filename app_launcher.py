import sys
from tkinter import Tk
from GUI import App

import xml.etree.ElementTree as Et


if __name__ == "__main__":
    # tree = Et.parse("E:\\Project\\nmai\waterpuzzle\\input\\levels.xml")
    # root = tree.getroot()
    # print(len(sys.argv))
    if len(sys.argv) == 2:
        level = [i for i in range(1, 41)]
        method = sys.argv[1].upper()
    elif len(sys.argv) == 3:
        level = [sys.argv[1]]
        method = sys.argv[2].upper()
    else:
        print("[Usage: app_launcher.py ")
    root = Tk()
    app = App(root)
    app.master.title("WaterSortGame")
    root.mainloop()

