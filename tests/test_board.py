import unittest
from tour.board import Board

class Test_TestBoard(unittest.TestCase):
    def test_get_right_moves_center(self):
        board = Board(3, 3)
        self.assertEqual(board.get_right_moves(), ((6, 5), (6, 3)))
        print("Here")

if __name__ == '__main__':
    unittest.main()