from tour.manager import Manager
from tour.pickler import Pickler

print("HERE")
manager = Pickler("tour.pickle").load()
if manager is None:
    manager = Manager()

print("Starting state:")
manager.print_state()
manager.depth_first_tour()

def __main__():
    print("here")
    # Manager().depth_first_tour()
    print("done")