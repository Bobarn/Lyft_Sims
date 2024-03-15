from abc import ABC, abstractmethod
# from battery import SpindlerBattery, NubbinBattery
# from engine. import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine
from tire.carrigan import CarriganSet
from tire.octoprime import OctoPrimeSet

class Car(ABC):
    def __init__(self, engine, battery, tire_set):
        self.engine = engine
        self.battery = battery
        self.tire_set = tire_set

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire_set.needs_service()


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, carrigan, tires):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire_set = CarriganSet(tires) if carrigan else OctoPrimeSet(tires)
        car = Car(engine, battery, tire_set)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, carrigan, tires):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire_set = CarriganSet(tires) if carrigan else OctoPrimeSet(tires)
        car = Car(engine, battery, tire_set)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, carrigan, tires):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire_set = CarriganSet(tires) if carrigan else OctoPrimeSet(tires)
        car = Car(engine, battery, tire_set)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, carrigan, tires):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire_set = CarriganSet(tires) if carrigan else OctoPrimeSet(tires)
        car = Car(engine, battery, tire_set)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, carrigan, tires):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire_set = CarriganSet(tires) if carrigan else OctoPrimeSet(tires)
        car = Car(engine, battery, tire_set)
        return car
