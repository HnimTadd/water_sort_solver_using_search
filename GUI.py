from tkinter import Button, Label, W, E, N, S, messagebox
# from PIL import Image, ImageT
import tkinter as tk
import socket, threading, sys, traceback, os


class App:
    def __init__(self, master):
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.handler)
        self.create_widgets()
        self.levels = None
        self.algorithm = None
        self.view = None
        self.pause = None
        self.start = None

    def create_widgets(self):
        self.start = Button(self.master, width=20, padx=3, pady=3)
        self.start["text"] = "Start"
        self.start["command"] = self.start_play
        self.start.grid(row=1, column=1, padx=2, pady=2)

        self.pause = Button(self.master, width=20, padx=3, pady=3)
        self.pause["text"] = "Pause"
        self.pause["command"] = self.pause
        self.pause.grid(row=1, column=2, padx=2, pady=2)

        self.view = Label(self.master, height=19)
        self.view.grid(row=0, column=0, columnspan=4, sticky=W + E + N + S, padx=5, pady=5)

    def start_play(self, levels, algorithm):
        """start_play game handle, call update frame method"""
        pass

    def update_frame(self, stage, action):
        pass

    def exit_client(self):
        self.master.destroy()

    def pause(self):
        pass

    def take_input(self, level):
        pass

    def handler(self):
        # self.pause()
        if messagebox.askokcancel("Quit", "Are you sure want to quit?"):
            self.exit_client()
        else:
            return

# root = tk.Tk()
# app = App(root)
# app.master.title("WaterSortGame")
# root.mainloop()
