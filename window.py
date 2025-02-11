from tkinter import Tk, BOTH, Canvas

class Window(Tk):
    def __init__(self, width=800, height=600):
        Tk.__init__(self)
        self.__root = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        Tk.update_idletasks(self)
        Tk.update(self)

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False