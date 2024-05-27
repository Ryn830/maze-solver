import unittest

from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        rows = 10
        cols = 12

        maze_1 = Maze(0, 0, rows, cols, 10, 10)

        self.assertEqual(len(maze_1.cells), rows)
        self.assertEqual(len(maze_1.cells[0]), cols)

        rows = 15
        cols = 20

        maze_2 = Maze(0, 0, rows, cols, 10, 10)

        self.assertEqual(len(maze_2.cells), rows)
        self.assertEqual(len(maze_2.cells[0]), cols)

    def test_break_entrance_and_exit(self):
        rows = 10
        cols = 12

        maze = Maze(0, 0, rows, cols, 10, 10)

        entrance_cell = maze.cells[0][0]
        exit_cell = maze.cells[maze.num_rows - 1][maze.num_cols - 1]

        self.assertFalse(entrance_cell.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)

    def test_reset_cells_visited(self):
        rows = 10
        cols = 12

        maze = Maze(0, 0, rows, cols, 10, 10)

        for row in range(0, rows):
            for col in range(0, cols):
                self.assertFalse(maze.cells[row][col].visited)


if __name__ == "__main__":
    unittest.main()
