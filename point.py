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

class Cell:
    def __init__(self, has_left_wall, has_top_wall, has_right_wall, has_bottom_wall, _x1, _y1, _x2, _y2, _win=None, visited=False):
        self.has_left_wall = has_left_wall
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = _x1
        self.y1 = _y1
        self.x2 = _x2
        self.y2 = _y2
        self.win = _win
        self.visited = visited

    def draw(self):
        if self.has_left_wall:
            self.win.canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill="black", width=2)
        else:
            self.win.canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill="white", width=2)
        if self.has_top_wall:
            self.win.canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill="black", width=2)
        else:
            self.win.canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill="white", width=2)
        if self.has_right_wall:
            self.win.canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill="black", width=2)
        else:
            self.win.canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill="white", width=2)
        if self.has_bottom_wall:
            self.win.canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill="black", width=2)
        else:
            self.win.canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill="white", width=2)

    def draw_move(self, to_cell, undo=False):
        # Calculate the center points of self and to_cell
        self_center_x = (self.x1 + self.x2) / 2
        self_center_y = (self.y1 + self.y2) / 2
        to_center_x = (to_cell.x1 + to_cell.x2) / 2
        to_center_y = (to_cell.y1 + to_cell.y2) / 2
        # Draw the line from the center of self to the center of to_cell
        if undo:
            self.win.canvas.create_line(self_center_x, self_center_y, to_center_x, to_center_y, fill="red", width=2)
        else:
            self.win.canvas.create_line(self_center_x, self_center_y, to_center_x, to_center_y, fill="gray", width=2)