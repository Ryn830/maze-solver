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


if __name__ == "__main__":
    unittest.main()
