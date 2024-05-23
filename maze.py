from time import sleep

from window import Window
from point import Point
from cell import Cell


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.cells = []
        self._create_cells()

    def _create_cells(self):
        for row in range(self.num_rows):
            new_row = []
            for col in range(self.num_cols):
                start = Point(
                    self.x1 + (col * self.cell_size_x),
                    self.y1 + (row * self.cell_size_y),
                )
                end = Point(
                    self.x1 + (col * self.cell_size_x) + self.cell_size_x,
                    self.y1 + (row * self.cell_size_y) + self.cell_size_y,
                )
                cell = Cell(self.win, start, end)
                cell.draw()
                new_row.append(cell)
            self.cells.append(new_row)
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(0.05)
