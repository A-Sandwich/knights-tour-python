import numpy as np

class Board:
    def __init__(self, starting_x, starting_y):
        self.board_size = (8, 8)
        self.cells = np.zeros((8, 8), dtype=int)
        self.cells[starting_x][starting_y] = 1
        self.last_move_number = 1
        self.last_move = (starting_x, starting_y)
        self.moves = [*self.get_right_moves(), *self.get_left_moves(), *self.get_down_moves(), *self.get_up_moves()]

    def get_next_move(self):
        for move in self.moves:
            if self.is_move_valid(move):
                return move
        return (-1, -1)

    def remove_invalid_moves(self):
        invalid_moves = []
        for move in self.moves:
            if not self.is_move_valid(move):
                invalid_moves.append(move)
                
        for invalid_move in invalid_moves:
            self.moves.remove(invalid_move)

    def get_right_moves(self):
        return ((self.last_move[0] + 2, self.last_move[1] + 1),  (self.last_move[0] + 2, self.last_move[1] - 1))
    
    def get_left_moves(self):
        return ((self.last_move[0] - 2, self.last_move[1] - 1), (self.last_move[0] - 2, self.last_move[1] + 1))
    
    def get_down_moves(self):
        return ((self.last_move[0] + 1, self.last_move[1] + 2), (self.last_move[0] - 1, self.last_move[1] + 2))
    
    def get_up_moves(self):
        return ((self.last_move[0] - 1, self.last_move[1] - 2), (self.last_move[0] + 1, self.last_move[1] - 2))

    def is_move_valid(self, move):
        return self.is_x_valid(move[0]) and self.is_y_valid(move[1]) and self.cells[move[0]][move[1]] == 0

    def is_x_valid(self, x):
        return x < self.board_size[0] and x >= 0
    
    def is_y_valid(self, y):
        return y < self.board_size[1] and y >= 0

    def get_next_move(self):
        pass

    def is_path_blocked(self):
        pass

    def is_tour_complete(self):
        pass