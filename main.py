from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(20, 20, 28, 38, 20, 20, win, 0)
    maze.solve_maze()

    win.wait_for_close()


main()
