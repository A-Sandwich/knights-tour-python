from tour.board import Board
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from datetime import datetime, timedelta
from tour.pickler import Pickler

class Manager:
    def __init__(self, board_size=8):
        print("init 🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕🆕")
        self.boards = [Board().seed_board_with_starting_position(0, 0, board_size)]
        self.iteration = 0
        self.failed_paths = 0
        self.elapsed_time = 0

    def save(self):
        pickler = Pickler("tour_progress.pickle")
        pickler.save(self)
        print("pickled 🥒🥒🥒🥒")
    
    def depth_first_tour(self):
        while len(self.boards) > 0 and not self.is_tour_complete():
            loop_start_time = time()
            furthest_board = self.boards[-1]
            next_move = furthest_board.get_next_move()
            if next_move == (-1, -1):
                self.boards.remove(furthest_board)
                self.failed_paths += 1
            else:
                next_board = Board().seed_board(furthest_board, next_move)
                self.boards.append(next_board)
            self.iteration += 1
            if self.iteration % 1250000 == 0:
                #self.save()
                self.print_state()
            self.elapsed_time += time() - loop_start_time
        print("Final board:")
        self.print_state()
        print("DONE 🤪🤪🤪🤪🤪")


    def print_state(self):
        print("Print state 🖨️🖨️🖨️🖨️🖨️🖨️")
        if (len(self.boards) <= 0):
            print("No boards left ⛓️‍💥⛓️‍💥⛓️‍💥⛓️‍💥")
            return
        print(self.boards[-1])
        print("🎠 Iteration: ", self.iteration)
        print("🏁 Boards: ", len(self.boards))
        print("🗺️ Failed paths: ", self.failed_paths)
        print(f"⏳ Time elapsed: {self.get_elapsed_time()}")
        print("\n\n")
    
    def get_elapsed_time(self):
        return str(timedelta(seconds=self.elapsed_time))

    def is_tour_complete(self):
        for board in self.boards:
            if board.is_tour_complete():
                print("IS COMPLETED 🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨")
                return True
        return False
    
def is_board_complete(board):
    return board.is_tour_complete()

if __name__ == '__main__':
    Manager().depth_first_tour()