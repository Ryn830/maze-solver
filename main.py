from window import Window
from point import Point
from line import Line


def main():
    win = Window(800, 600)

    start = Point(100, 100)
    end = Point(200, 300)

    line = Line(start, end)

    win.draw_line(line, "black")

    win.wait_for_close()


main()
