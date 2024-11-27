from tour.board import Board
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time

class Manager:
    def __init__(self):
        self.boards = [Board().seed_board_with_starting_position(3, 3)]
        self.iteration = 0
        self.failed_paths = 0
        self.start_time = time()
        self.furthest_move = 0
    
    def depth_first_tour(self):
        while len(self.boards) > 0 and not self.is_tour_complete():
            furthest_board = self.boards[-1]
            next_move = furthest_board.get_next_move()
            if next_move == (-1, -1):
                if furthest_board.last_move_number > self.furthest_move:
                    self.furthest_move = furthest_board.last_move_number
                self.boards.pop()
                self.failed_paths += 1
                continue
            next_board = Board().seed_board(furthest_board, next_move)
            self.boards.append(next_board)
            self.iteration += 1
            if self.iteration % 500000 == 0:
                self.print_state()
        print("Final board:")
        self.print_state()
        print("DONE 🤪🤪🤪🤪🤪")


    def print_state(self):
        print(self.boards[-1])
        print("🎠Iteration: ", self.iteration)
        print("🏁Boards: ", len(self.boards))
        print("🗺️Failed paths: ", self.failed_paths)
        print("♟️Furthest move: ", self.furthest_move)
        print("⏳Time elapsed in seconds: ", time() - self.start_time)
        print("\n\n")

    def is_tour_complete(self):
        for board in self.boards:
            if board.is_tour_complete():
                print("IS COMPLETED 🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨")
                return True
        return False
    
    ### def is_tour_complete(self):
        results = []
        with ThreadPoolExecutor(max_workers=14) as executor:
            futures = [executor.submit(is_board_complete, board) for board in self.boards]
            for future in as_completed(futures):
                results.append(future.result())
        for result in results:
            if result:
                return True
    ###
def is_board_complete(board):
    return board.is_tour_complete()


if __name__ == '__main__':
    Manager().depth_first_tour()