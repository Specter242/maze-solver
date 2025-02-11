from tkinter import Tk, BOTH, Canvas
from window import Window
from point import line

def main():
    win = Window(800, 600)
    line1 = line(100, 100, 200, 200)
    win.draw_line(line1)
    win.wait_for_close()

main()