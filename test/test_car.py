import unittest
from datetime import datetime, date

from car import Car
from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan import CarriganSet
from tire.octoprime import OctoPrimeSet


class TestCalliope(unittest.TestCase):
    def test_battery_and_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2021-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)

        self.assertTrue(car.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

    def test_battery_should_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2021-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())


    def test_tires_should_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.9, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

class TestGlissade(unittest.TestCase):
    def test_battery_and_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2021-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)

        self.assertTrue(car.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

    def test_battery_should_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2021-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())


    def test_tires_should_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.9, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

class TestPalindrome(unittest.TestCase):
    def test_battery_and_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2021-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)

        self.assertTrue(car.needs_service())

    def test_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

    def test_battery_should_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2021-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

    def test_tires_should_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = SpindlerBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.9, 0.7]
        tire_set = CarriganSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

class TestRorschach(unittest.TestCase):
    def test_battery_and_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2020-01-31")
        battery = NubbinBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = OctoPrimeSet(tire_wear)

        car = Car(engine, battery, tire_set)

        self.assertTrue(car.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = NubbinBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = OctoPrimeSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = NubbinBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = OctoPrimeSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

    def test_battery_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2020-01-31")
        battery = NubbinBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = OctoPrimeSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = NubbinBattery(current_date, last_service_date)

        tire_wear = [0.5, 0.9, 0.9, 0.7]
        tire_set = OctoPrimeSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

class TestThovex(unittest.TestCase):
    def test_battery_and_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2020-01-31")
        battery = NubbinBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = OctoPrimeSet(tire_wear)

        car = Car(engine, battery, tire_set)

        self.assertTrue(car.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2023-01-31")
        battery = NubbinBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = OctoPrimeSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2023-01-31")
        battery = NubbinBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = OctoPrimeSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

    def test_battery_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2020-01-31")
        battery = NubbinBattery(current_date, last_service_date)

        tire_wear = [0.1, 0.5, 0.3, 0.7]
        tire_set = OctoPrimeSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        current_date = date.fromisoformat("2024-03-15")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = NubbinBattery(current_date, last_service_date)

        tire_wear = [0.5, 0.9, 0.9, 0.7]
        tire_set = OctoPrimeSet(tire_wear)

        car = Car(engine, battery, tire_set)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()
