import unittest

from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        cols = 12
        rows = 10

        maze = Maze(0, 0, cols, rows, 10, 10)

        self.assertEqual(len(maze.cells), cols)
        self.assertEqual(len(maze.cells[0]), rows)


if __name__ == "__main__":
    unittest.main()
