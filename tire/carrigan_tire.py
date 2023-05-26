from abc import ABC

from tire_class import Tire

class CarriganTire(Tire,ABC):
    def __init__(self,tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        for n in self.tire_wear:
            if n>=0.9:
                return True
        return False