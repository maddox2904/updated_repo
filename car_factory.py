from car import Car

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class CarFactory:

    def create_calliope(self, last_service_date, current_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        tire = CarriganTire(tire_wear)
        newCar = Car(engine,battery,tire)
        return newCar

    def create_glissade(self, last_service_date, current_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        tire = CarriganTire(tire_wear)
        newCar = Car(engine,battery,tire)
        return newCar
    
    def create_palindrome(self, last_service_date, current_date, warning_light_is_on, tire_wear) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date,current_date)
        tire = CarriganTire(tire_wear)
        newCar = Car(engine,battery,tire)
        return newCar

    def create_rorschach(self, last_service_date, current_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        tire = CarriganTire(tire_wear)
        newCar = Car(engine,battery,tire)
        return newCar
    
    def create_thovex(self, last_service_date, current_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        tire = CarriganTire(tire_wear)
        newCar = Car(engine,battery,tire)
        return newCar