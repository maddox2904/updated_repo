from abc import ABC
from engine_class import Engine
from battery_class import Battery

class Car(ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool: 
        return self.battery.needs_service() or self.engine.needs_service()
