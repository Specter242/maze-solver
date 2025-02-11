from tkinter import Tk, BOTH, Canvas
from point import Point, line, Cell
from window import Window
import time, random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        if self.seed != None:
            random.seed(self.seed)
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
                has_left_wall = True
                has_top_wall = True
                has_right_wall = True
                has_bottom_wall = True
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
        
    def _break_walls_r(self, i, j):
        if i < 0 or i >= self.num_rows or j < 0 or j >= self.num_cols:
            return
        cell = self.cells[i * self.num_cols + j]
        if cell.visited:
            return
        cell.visited = True
        neighbors = []
        if i > 0 and not self.cells[(i - 1) * self.num_cols + j].visited:
            neighbors.append((i - 1, j))
        if i < self.num_rows - 1 and not self.cells[(i + 1) * self.num_cols + j].visited:
            neighbors.append((i + 1, j))
        if j > 0 and not self.cells[i * self.num_cols + j - 1].visited:
            neighbors.append((i, j - 1))
        if j < self.num_cols - 1 and not self.cells[i * self.num_cols + j + 1].visited:
            neighbors.append((i, j + 1))
        if len(neighbors) > 0:
            next_i, next_j = random.choice(neighbors)
            next_cell = self.cells[next_i * self.num_cols + next_j]
            if next_i < i:
                cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif next_i > i:
                cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif next_j < j:
                cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif next_j > j:
                cell.has_right_wall = False
                next_cell.has_left_wall = False
            self._draw_cells()
            self._break_walls_r(next_i, next_j)