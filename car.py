from abc import ABC
from engine_class import Engine
from battery_class import Battery
from tire_class import Tire

class Car(ABC):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool: 
        return self.battery.needs_service() or self.engine.needs_service() or self.tire.needs_service()
