import unittest

from tire.carrigan import CarriganSet


class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.3, 0.4, 0.9, 0.6]
        tire_set = CarriganSet(tire_wear)
        self.assertTrue(tire_set.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)
        self.assertFalse(tire_set.needs_service())
