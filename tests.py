import unittest
from maze import Maze
from window import Window
from tkinter import Tk

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.win = Window(Tk(), 800, 600)
        self.maze = Maze(0, 0, 10, 10, 20, 20, self.win, seed=42)

    def test_maze_initialization(self):
        self.assertEqual(len(self.maze.cells), 100)
        self.assertEqual(self.maze.cells[0].has_top_wall, False)
        self.assertEqual(self.maze.cells[-1].has_bottom_wall, False)

    def test_maze_cells(self):
        for cell in self.maze.cells:
            self.assertTrue(cell.has_left_wall)
            self.assertTrue(cell.has_top_wall)
            self.assertTrue(cell.has_right_wall)
            self.assertTrue(cell.has_bottom_wall)

    def test_break_walls_r(self):
        self.maze._reset_cells_visited()
        self.maze._break_walls_r(0, 0)
        visited_cells = [cell for cell in self.maze.cells if cell.visited]
        self.assertEqual(len(visited_cells), 100)

    def test_reset_cells_visited(self):
        self.maze._break_walls_r(0, 0)
        self.maze._reset_cells_visited()
        for cell in self.maze.cells:
            self.assertFalse(cell.visited)

if __name__ == '__main__':
    unittest.main()