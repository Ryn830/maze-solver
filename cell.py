from typing import List

from point import Point
from line import Line
from window import Window


class Cell:
    def __init__(
        self, win: Window, start: Point, end: Point, row: int, col: int
    ) -> None:
        # Coordinates on grid. Top left and bottom right
        # note: (0,0) is in the top right and (∞,∞) is in the bottom left
        self._x1 = start.x
        self._y1 = start.y
        self._x2 = end.x
        self._y2 = end.y

        self.row = row
        self.col = col

        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

        # True if cell has had it's walls broken by maze walking algorithm
        # Or used in solving the maze
        self.visited = False

        self.win = win

    def __repr__(self) -> str:
        return f"{(self.row, self.col, 'X' if self.visited else 'O')}"

    def draw_wall(self, start: Point, end: Point, color="black"):
        if self.win is None:
            return

        wall_start = Point(start.x, start.y)
        wall_end = Point(end.x, end.y)
        wall_line = Line(wall_start, wall_end)
        self.win.draw_line(wall_line, color)

    def draw_walls(self):
        if self.win is None:
            return

        if self.has_top_wall:
            self.draw_wall(Point(self._x1, self._y1), Point(self._x2, self._y1))

        if self.has_right_wall:
            self.draw_wall(Point(self._x2, self._y1), Point(self._x2, self._y2))

        if self.has_bottom_wall:
            self.draw_wall(Point(self._x1, self._y2), Point(self._x2, self._y2))

        if self.has_left_wall:
            self.draw_wall(Point(self._x1, self._y1), Point(self._x1, self._y2))

    # Removing a wall is drawing over it
    def remove_walls(self, directions: List[str]):
        for direction in directions:
            if direction == "top":
                self.has_top_wall = False
                self.draw_wall(
                    Point(self._x1, self._y1), Point(self._x2, self._y1), "white"
                )

            if direction == "right":
                self.has_right_wall = False
                self.draw_wall(
                    Point(self._x2, self._y1), Point(self._x2, self._y2), "white"
                )

            if direction == "bottom":
                self.has_bottom_wall = False
                self.draw_wall(
                    Point(self._x1, self._y2), Point(self._x2, self._y2), "white"
                )

            if direction == "left":
                self.has_left_wall = False
                self.draw_wall(
                    Point(self._x1, self._y1), Point(self._x1, self._y2), "white"
                )

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
