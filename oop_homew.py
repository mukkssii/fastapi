from abc import ABC, abstractmethod


class CONFIG:
    FUEL_VOLUME = 60


class Vehicle(ABC):
    def __init__(self, brand, fuel_volume, fuel_remain, speed, mileage):
        self.brand = brand
        self.fuel_volume = fuel_volume
        self.fuel_remain = fuel_remain
        self.speed = speed
        self.mileage = mileage

    def refill(self, fuel):
        print('refilling')
        self.fuel_remain += fuel
        if self.fuel_remain > CONFIG.FUEL_VOLUME:
            self.fuel_remain = CONFIG.FUEL_VOLUME

    def fuel_transfusing(self, other, fuel_volume):
        print('Transfusing fuel')
        self.fuel_remain -= fuel_volume
        other.fuel_remain += fuel_volume
        if fuel_volume > self.fuel_remain:
            self.fuel_remain = 0
            other.fuel_remain += self.fuel_remain
        if other.fuel_remain > CONFIG.FUEL_VOLUME:
            other.fuel_remain = CONFIG.FUEL_VOLUME

    @abstractmethod
    def __str__(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, fuel_volume, fuel_remain, speed, mileage, passengers, airbags=True):
        super().__init__(brand, fuel_volume, fuel_remain, speed, mileage)
        self.passengers = passengers
        self.airbags = airbags

    def __str__(self):
        return f'Now your vehicle has {self.fuel_remain} liters fuel in it'


class Motorcycle(Vehicle):
    def __init__(self, brand, fuel_volume, fuel_remain, speed, mileage, carriage=True):
        super().__init__(brand, fuel_volume, fuel_remain, speed, mileage)
        self.carriage = carriage

    def __str__(self):
        return f'Now your vehicle has {self.fuel_remain} liters fuel in it'


car = Car(brand='BMW', fuel_volume=CONFIG.FUEL_VOLUME, fuel_remain=20, speed=120, mileage=592, passengers=4)
motorcycle = Motorcycle(brand='Mercedes', fuel_volume=CONFIG.FUEL_VOLUME, fuel_remain=20, speed=120, mileage=468)
car.refill(fuel=3)
motorcycle.refill(fuel=30)
motorcycle.fuel_transfusing(car, 23)
car.fuel_transfusing(motorcycle, 4)
print(car)
print(motorcycle)
