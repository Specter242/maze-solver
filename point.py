from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas, fill_color="black", x1=0, y1=0, x2=0, y2=0):
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)