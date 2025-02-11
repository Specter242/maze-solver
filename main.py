from tkinter import Tk, BOTH, Canvas
from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 50, 50, win)
    win.wait_for_close()
    

main()