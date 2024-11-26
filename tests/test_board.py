import unittest
from tour.board import Board

class Test_TestBoard(unittest.TestCase):
    def test_get_right_moves_center(self):
        board = Board(3, 3)
        result = board.get_right_moves()
        self.assertTrue((5, 2) in result)
        self.assertTrue((5, 4) in result)

    def test_get_left_moves_center(self):
        board = Board(3, 3)
        result = board.get_left_moves()
        self.assertTrue((1, 2) in result)
        self.assertTrue((1, 4) in result)

    def test_get_up_moves_center(self):
        board = Board(3, 3)
        result = board.get_up_moves()
        self.assertTrue((2, 1) in result)
        self.assertTrue((4, 1) in result)

    def test_get_down_moves_center(self):
        board = Board(3, 3)
        result = board.get_down_moves()
        self.assertTrue((2, 5) in result)
        self.assertTrue((4, 5) in result)

if __name__ == '__main__':
    unittest.main()