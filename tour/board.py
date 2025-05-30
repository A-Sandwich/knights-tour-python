import numpy as np
import copy

class Board:
    def __init__(self):
        pass
    

    def seed_board_with_starting_position(self, starting_x, starting_y, board_size=8):
        self.board_size = (board_size, board_size)
        self.cells = np.zeros((board_size, board_size), dtype=int)
        self.cells[starting_x][starting_y] = 1
        self.last_move_number = 1
        self.last_move = (starting_x, starting_y)
        self.moves = self.get_moves(self.last_move)
        return self

    def seed_board(self, board, move):
        self.board_size = board.board_size
        self.cells = copy.deepcopy(board.cells)
        self.cells[move[0]][move[1]] = board.last_move_number + 1
        self.last_move_number = board.last_move_number + 1
        self.last_move = move
        self.moves = self.get_moves(self.last_move)
        return self

    # My intent is that we just remove taken paths and once we are out of moves we know this path is not valid
    def get_next_move(self):
        self.moves = self.remove_invalid_moves(self.moves)
        
        number_of_possible_moves = 99999
        selected_move = (-1, -1)
        for move in self.moves:
            moves = self.get_moves(move)
            moves = self.remove_invalid_moves(moves)
            if len(moves) < number_of_possible_moves:
                number_of_possible_moves = len(moves)
                selected_move = move
        if selected_move != (-1, -1):
            self.moves.remove(selected_move)
        return selected_move
        

    def remove_invalid_moves(self, moves):
        invalid_moves = []
        for move in moves:
            if not self.is_move_valid(move):
                invalid_moves.append(move)
                
        for invalid_move in invalid_moves:
            moves.remove(invalid_move)
        return moves
    
    def get_moves(self, move):
        return [
            (move[0] + 2, move[1] + 1),
            (move[0] + 2, move[1] - 1),

            (move[0] - 2, move[1] - 1),
            (move[0] - 2, move[1] + 1),

            (move[0] + 1, move[1] + 2),
            (move[0] - 1, move[1] + 2),

            (move[0] - 1, move[1] - 2),
            (move[0] + 1, move[1] - 2)
        ]
    def is_move_valid(self, move):
        move_is_on_board = self.is_x_valid(move[0]) and self.is_y_valid(move[1]) and self.cells[move[0]][move[1]] == 0
        return move_is_on_board

    def is_x_valid(self, x):
        return x < self.board_size[0] and x >= 0
    
    def is_y_valid(self, y):
        return y < self.board_size[1] and y >= 0

    def is_path_blocked(self):
        if len(self.moves) == 0 and not self.is_tour_complete():
            return True
        return False

    def is_tour_complete(self):
        for column in self.cells:
            for cell in column:
                if cell == 0:
                    return False
        print("Tour is complete! ✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅")
        return True
    
    
    def __str__(self):
        printed_board = ""
        for column in self.cells:
            for cell in column:
                printed_board += f"{cell:04d}|"
            printed_board += "\n"
        return printed_board