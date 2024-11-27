from tour.board import Board

class Manager:
    def __init__(self):
        self.boards = [Board().seed_board_with_starting_position(3, 3)]
    
    def depth_first_tour(self):
        iteration = 0
        while len(self.boards) > 0 and not self.is_tour_complete():
            furthest_board = self.boards[-1]
            next_move = furthest_board.get_next_move()
            if next_move == (-1, -1):
                self.boards.pop()
                continue
            next_board = Board().seed_board(furthest_board, next_move)
            self.boards.append(next_board)
            iteration += 1
            if iteration % 1000000 == 0:
                print(self.boards[-1])
                print("Iteration: ", iteration)
        print("Final board:")
        print(self.boards[-1])
        print("DONE 🤪🤪🤪🤪🤪")


    def is_tour_complete(self):
        for board in self.boards:
            if board.is_tour_complete():
                return True
        return False

if __name__ == '__main__':
    Manager().depth_first_tour()