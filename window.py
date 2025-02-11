from tkinter import Tk, BOTH, Canvas
from point import Point, line

class Window(Tk):
    def __init__(self, width=800, height=600):
        Tk.__init__(self)
        self.width = width
        self.height = height
        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        Tk.update_idletasks(self)
        Tk.update(self)

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color, line.x1, line.y1, line.x2, line.y2)