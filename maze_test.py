import unittest

from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        cols = 12
        rows = 10

        maze_1 = Maze(0, 0, cols, rows, 10, 10)

        self.assertEqual(len(maze_1.cells), cols)
        self.assertEqual(len(maze_1.cells[0]), rows)

        cols = 20
        rows = 15

        maze_2 = Maze(0, 0, cols, rows, 10, 10)

        self.assertEqual(len(maze_2.cells), cols)
        self.assertEqual(len(maze_2.cells[0]), rows)

    def test_break_entrance_and_exit(self):
        cols = 12
        rows = 10

        maze = Maze(0, 0, cols, rows, 10, 10)
        maze._break_entrance_and_exit()

        entrance_cell = maze.cells[0][0]
        exit_cell = maze.cells[maze.num_rows - 1][maze.num_cols - 1]

        self.assertFalse(entrance_cell.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)


if __name__ == "__main__":
    unittest.main()
