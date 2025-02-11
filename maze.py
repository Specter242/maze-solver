from tkinter import Tk, BOTH, Canvas
from point import Point, line, Cell
from window import Window
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x1 = self.x1 + col * self.cell_size_x
                y1 = self.y1 + row * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                has_left_wall = col == 0
                has_top_wall = row == 0
                has_right_wall = col == self.num_cols - 1
                has_bottom_wall = row == self.num_rows - 1
                cell = Cell(has_left_wall, has_top_wall, has_right_wall, has_bottom_wall, x1, y1, x2, y2, self.win)
                self.cells.append(cell)
        self._draw_cells()

    def _draw_cells(self):
        for cell in self.cells:
            cell.draw()
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self.cells[0].has_top_wall = False
        self.cells[-1].has_bottom_wall = False
        self._draw_cells()
        
        