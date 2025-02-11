from tkinter import Tk, BOTH, Canvas
from window import Window
from maze import Maze

def main():
    cell_size = 50
    maze_width = 50
    maze_height = 50
    window_width = maze_width * cell_size
    window_height = maze_height * cell_size
    
    win = Window(window_width, window_height)
    maze = Maze(maze_width, maze_height, 10, 10, cell_size, cell_size, win)
    maze._break_walls_r(0, 0)
    win.wait_for_close()
    

main()