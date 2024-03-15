import unittest
from datetime import date

from battery import NubbinBattery


class TestNubbin(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2020-01-31")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
