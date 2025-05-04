from tour.manager import Manager
from tour.pickler import Pickler
import os
manager = None
#if os.path.exists("tour_progress.pickle"):
#    manager = Pickler("tour_progress.pickle").load()
if manager is None:
    manager = Manager(64)

print("Starting state:")
manager.print_state()
manager.depth_first_tour()

def __main__():
    print("here")
    # Manager().depth_first_tour()
    print("done")