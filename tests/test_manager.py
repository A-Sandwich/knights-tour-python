import unittest
from tour.manager import Manager

class Test_TestManager(unittest.TestCase):
    def test_depth_first_tour(self):
        manager = Manager()
        manager.depth_first_tour()
        self.assertTrue(manager.is_tour_complete())