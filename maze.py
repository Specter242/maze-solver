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
        self.cells[i * self.num_cols + j].visited = True
        while True:
            neighbors = []
            if i > 0 and not self.cells[(i - 1) * self.num_cols + j].visited:
                neighbors.append((i - 1, j))
            if i < self.num_rows - 1 and not self.cells[(i + 1) * self.num_cols + j].visited:
                neighbors.append((i + 1, j))
            if j > 0 and not self.cells[i * self.num_cols + j - 1].visited:
                neighbors.append((i, j - 1))
            if j < self.num_cols - 1 and not self.cells[i * self.num_cols + j + 1].visited:
                neighbors.append((i, j + 1))
            if not neighbors:
                return
            next_i, next_j = random.choice(neighbors)
            # Remove the wall between the current cell and the chosen cell
            if next_i == i - 1:  # Moving up
                self.cells[i * self.num_cols + j].has_top_wall = False
                self.cells[next_i * self.num_cols + next_j].has_bottom_wall = False
            elif next_i == i + 1:  # Moving down
                self.cells[i * self.num_cols + j].has_bottom_wall = False
                self.cells[next_i * self.num_cols + next_j].has_top_wall = False
            elif next_j == j - 1:  # Moving left
                self.cells[i * self.num_cols + j].has_left_wall = False
                self.cells[next_i * self.num_cols + next_j].has_right_wall = False
            elif next_j == j + 1:  # Moving right
                self.cells[i * self.num_cols + j].has_right_wall = False
                self.cells[next_i * self.num_cols + next_j].has_left_wall = False
            self._draw_cells()
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for cell in self.cells:
            cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self.animate()
        self.cells[i * self.num_cols + j].visited = True
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
        neighbors = []
        if i > 0 and not self.cells[(i - 1) * self.num_cols + j].visited and not self.cells[i * self.num_cols + j].has_top_wall:
            neighbors.append((i - 1, j))
        if i < self.num_rows - 1 and not self.cells[(i + 1) * self.num_cols + j].visited and not self.cells[(i + 1) * self.num_cols + j].has_top_wall:
            neighbors.append((i + 1, j))
        if j > 0 and not self.cells[i * self.num_cols + j - 1].visited and not self.cells[i * self.num_cols + j].has_left_wall:
            neighbors.append((i, j - 1))
        if j < self.num_cols - 1 and not self.cells[i * self.num_cols + j + 1].visited and not self.cells[i * self.num_cols + j + 1].has_left_wall:
            neighbors.append((i, j + 1))
        for next_i, next_j in neighbors:
            self.cells[i * self.num_cols + j].draw_move(self.cells[next_i * self.num_cols + next_j])
            if self._solve_r(next_i, next_j):
                return True
            else:
                self.cells[next_i * self.num_cols + next_j].draw_move(self.cells[i * self.num_cols + j], undo=True)
        self.cells[i * self.num_cols + j].visited = False
        return False
    