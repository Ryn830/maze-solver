from window import Window
from point import Point
from line import Line
from cell import Cell


def main():
    win = Window(800, 600)

    start = Point(100, 100)
    end = Point(200, 300)

    line = Line(start, end)

    win.draw_line(line, "black")

    cell = Cell(win, start, end)
    cell.has_top_wall = False
    cell.draw()

    win.wait_for_close()


main()
