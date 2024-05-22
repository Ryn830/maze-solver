from window import Window
from point import Point
from line import Line
from cell import Cell


def main():
    win = Window(800, 600)

    start_p1 = Point(100, 100)
    end_p1 = Point(200, 200)
    cell_1 = Cell(win, start_p1, end_p1)
    cell_1.draw()

    start_p2 = Point(400, 400)
    end_p2 = Point(500, 500)
    cell_2 = Cell(win, start_p2, end_p2)
    cell_2.draw()

    cell_1.draw_move(cell_2)

    win.wait_for_close()


main()
