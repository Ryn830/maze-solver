from time import sleep
from typing import Union, List

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
        win: Union[Window, None] = None,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.cells: List[List[Cell]] = []
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
                cell.draw_walls()
                new_row.append(cell)
            self.cells.append(new_row)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self.cells[0][0]
        entrance_cell.remove_walls(["top"])

        exit_cell = self.cells[self.num_rows - 1][self.num_cols - 1]
        exit_cell.remove_walls(["bottom"])
