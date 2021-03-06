"""
доработайте базовый класс base.Vehicle:

добавьте атрибуты weight, started, fuel, fuel_consumption 
со значениями по умолчанию

добавьте инициализатор для установки weight, fuel, 
fuel_consumption

добавьте метод start. При вызове этого метода 
необходимо проверить состояние started. 
И если не started, то нужно проверить, 
что топлива больше нуля, и обновить состояние started, 
иначе нужно выкинуть исключение exceptions.LowFuelError

добавьте метод move, который проверяет, 
что достаточно топлива для преодоления переданной дистанции, 
и изменяет количество оставшегося топлива, иначе 
выкидывает исключение exceptions.NotEnoughFuel


"""
import sys
#print(sys.path)
sys.path.append('../')

from abc import ABC
#from homework_02.exceptions import LowFuelError, NotEnoughFuel
#import exceptions
from homework_02 import exceptions

class Vehicle(ABC):
    
    #weight = 1000
    #started = False
    #fuel = 10
    #fuel_consumption = 10

    def __init__(self, weight=0, fuel=0, fuel_consumption=0, started = False) :
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self) :
        if self.fuel > 0 and self.started is False :
            self.started = True
        if self.fuel <= 0 and self.started is False :
            raise exceptions.LowFuelError
            

    def move(self, distance) :
        fuel_needed = self.fuel_consumption * distance
        if self.fuel - fuel_needed >= 0 :
            self.fuel -= fuel_needed
        else :
            raise exceptions.NotEnoughFuel


if __name__ == "__main__" :
    #my_car = Vehicle(fuel=100)
    my_car = Vehicle(fuel=-10)

    print(my_car.fuel)
    print(my_car.started)

    my_car.start()
    print(my_car.started)

    #my_car.move(5)
    #print(my_car.fuel)







