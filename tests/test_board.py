import unittest
import copy
from tour.board import Board

class Test_TestBoard(unittest.TestCase):
    def test_get_right_moves_center(self):
        board = Board().seed_board_with_starting_position(3, 3)
        result = board.get_right_moves()
        self.assertTrue((5, 2) in result)
        self.assertTrue((5, 4) in result)

    def test_get_left_moves_center(self):
        board = Board().seed_board_with_starting_position(3, 3)
        result = board.get_left_moves()
        self.assertTrue((1, 2) in result)
        self.assertTrue((1, 4) in result)

    def test_get_up_moves_center(self):
        board = Board().seed_board_with_starting_position(3, 3)
        result = board.get_up_moves()
        self.assertTrue((2, 1) in result)
        self.assertTrue((4, 1) in result)

    def test_get_down_moves_center(self):
        board = Board().seed_board_with_starting_position(3, 3)
        result = board.get_down_moves()
        self.assertTrue((2, 5) in result)
        self.assertTrue((4, 5) in result)
    
    def test_is_move_valid(self):
        board = Board().seed_board_with_starting_position(3, 3)
        self.assertTrue(board.is_move_valid((0, 0)))
        self.assertTrue(board.is_move_valid((7, 7)))
        self.assertTrue(board.is_move_valid((0, 7)))
        self.assertTrue(board.is_move_valid((7, 0)))
        self.assertFalse(board.is_move_valid((-1, 0)))
        self.assertFalse(board.is_move_valid((0, -1)))
        self.assertFalse(board.is_move_valid((8, 8)))
        self.assertFalse(board.is_move_valid((0, 8)))
        self.assertFalse(board.is_move_valid((8, 0)))
        
    def test_remove_invalid_moves(self):
        board = Board().seed_board_with_starting_position(0, 0)
        all_moves = copy.deepcopy(board.moves)
        invalid_moves = []
        for move in all_moves:
            if move[0] < 0 or move[0] >= board.board_size[0] or move[1] < 0 or move[1] > board.board_size[1]:
                invalid_moves.append(move)
        board.remove_invalid_moves()
        self.assertNotEqual(all_moves, board.moves)
        self.assertTrue(len(all_moves) != len(board.moves))
        for invalid_move in invalid_moves:
            self.assertFalse(invalid_move in board.moves)
        
if __name__ == '__main__':

    unittest.main()