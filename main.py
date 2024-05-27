from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 5, 7, 100, 100, win, 0)
    maze._break_entrance_and_exit()
    maze._break_walls()

    win.wait_for_close()


main()
