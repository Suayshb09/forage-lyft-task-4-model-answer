from typing import List

# Define the ServiceCriteria interface
class ServiceCriteria:
    def check_service(self, miles_or_years: int) -> bool:
        pass

# Define the Battery class (common to all batteries)
class Battery(ServiceCriteria):
    def check_service(self, miles_or_years: int) -> bool:
        pass

# SpindlerBattery class (inherits from Battery)
class SpindlerBattery(Battery):
    def check_service(self, miles_or_years: int) -> bool:
        return miles_or_years >= 3

# Tires interface
class Tires(ServiceCriteria):
    def check_service(self, wear_array: List[float]) -> bool:
        pass

# CarriganTires class (inherits from Tires)
class CarriganTires(Tires):
    def check_service(self, wear_array: List[float]) -> bool:
        return any(wear >= 0.9 for wear in wear_array)

# OctoprimeTires class (inherits from Tires)
class OctoprimeTires(Tires):
    def check_service(self, wear_array: List[float]) -> bool:
        return sum(wear_array) >= 3

# CarModel class
class CarModel:
    def __init__(self, engine: ServiceCriteria, tires: Tires):
        self.engine = engine
        self.tires = tires

    def check_service(self, miles_or_years: int) -> bool:
        return self.engine.check_service(miles_or_years)

    def check_tire_service(self, wear_array: List[float]) -> bool:
        return self.tires.check_service(wear_array)

# Example usage
spindler_battery = SpindlerBattery()
print(spindler_battery.check_service(2))  # False (No service required in 2 years)
print(spindler_battery.check_service(3))  # True (Service required after 3 years)

carrigan_tires = CarriganTires()
wear_array = [0.8, 0.7, 0.9, 0.6]
print(carrigan_tires.check_service(wear_array))  # True (Service required due to tire wear)
