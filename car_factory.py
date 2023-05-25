from car import Car

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:

    def create_calliope(self, last_service_date, current_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        newCar = Car(engine,battery)
        return newCar

    def create_glissade(self, last_service_date, current_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        newCar = Car(engine,battery)
        return newCar
    
    def create_palindrome(self, last_service_date, current_date, warning_light_is_on) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date,current_date)
        newCar = Car(engine,battery)
        return newCar

    def create_rorschach(self, last_service_date, current_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        newCar = Car(engine,battery)
        return newCar
    
    def create_thovex(self, last_service_date, current_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        newCar = Car(engine,battery)
        return newCar