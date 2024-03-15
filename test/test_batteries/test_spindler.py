import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindler(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2021-01-31")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
