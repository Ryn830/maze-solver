from point import Point
from line import Line
from window import Window


class Cell:
    def __init__(self, win: Window, start: Point, end: Point) -> None:
        self._x1 = start.x
        self._y1 = start.y
        self._x2 = end.x
        self._y2 = end.y

        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

        self.win = win

    def draw(self):
        if self.has_top_wall:
            top_start = Point(self._x1, self._y1)
            top_end = Point(self._x2, self._y1)
            top_line = Line(top_start, top_end)
            self.win.draw_line(top_line)

        if self.has_right_wall:
            right_start = Point(self._x2, self._y1)
            right_end = Point(self._x2, self._y2)
            right_line = Line(right_start, right_end)
            self.win.draw_line(right_line)

        if self.has_bottom_wall:
            bottom_start = Point(self._x1, self._y2)
            bottom_end = Point(self._x2, self._y2)
            bottom_line = Line(bottom_start, bottom_end)
            self.win.draw_line(bottom_line)

        if self.has_left_wall:
            left_start = Point(self._x1, self._y1)
            left_end = Point(self._x1, self._y2)
            left_line = Line(left_start, left_end)
            self.win.draw_line(left_line)

    def draw_move(self, to_cell, undo=False):
        start_center = Point(
            abs(self._x2 - self._x1) / 2 + self._x1,
            abs(self._y2 - self._y1) / 2 + self._y1,
        )
        end_center = Point(
            abs(to_cell._x2 - to_cell._x1) / 2 + to_cell._x1,
            abs(to_cell._y2 - to_cell._y1) / 2 + to_cell._y1,
        )

        path = Line(start_center, end_center)
        self.win.draw_line(path, "gray" if undo else "red")
