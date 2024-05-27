from time import sleep
from typing import Union, List
from random import seed, shuffle

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
        random_seed: int = None,
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

        seed(random_seed)

        self._break_entrance_and_exit()
        self._break_walls()

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
                cell = Cell(self.win, start, end, row, col)
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

    """
    Possible directions:
            (i,j+1)
    (i-1,j) (i,j  ) (i+1,j)
            (i,j-1)
    """

    def _break_walls(self, draw_move: bool = False, i: int = 0, j: int = 0):
        current_cell = self.cells[i][j]
        current_cell.visited = True

        while True:
            directions = [
                (i, j + 1, "right"),
                (i, j - 1, "left"),
                (i + 1, j, "bottom"),
                (i - 1, j, "top"),
            ]

            possible_directions = []

            for direction in directions:
                row = direction[0]
                col = direction[1]
                if row < 0 or row >= self.num_rows:
                    continue

                if col < 0 or col >= self.num_cols:
                    continue

                if self.cells[row][col].visited == False:
                    possible_directions.append(direction)

            if len(possible_directions) == 0:
                return

            shuffle(possible_directions)
            (next_row, next_col, direction) = possible_directions.pop(0)
            current_cell.remove_walls([direction])
            if draw_move:
                current_cell.draw_move(self.cells[next_row][next_col])
            self._break_walls(draw_move, next_row, next_col)
