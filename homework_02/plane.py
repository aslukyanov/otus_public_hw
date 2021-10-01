"""
создайте класс `Plane`, наследник `Vehicle`
"""

import sys
#print(sys.path)
sys.path.append('../')

#from homework_02 import base
#from base import Vehicle
from homework_02 import exceptions
from homework_02.base import Vehicle




class Plane(Vehicle) :
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0, cargo=0) :
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo
        
    def load_cargo(self, val) :
        if val + self.cargo < self.max_cargo :
            self.cargo += val
        else :
            raise exceptions.CargoOverload

    def remove_all_cargo(self) :
        return_value = self.cargo
        self.cargo = 0
        return return_value
#weight=1000, fuel=0, fuel_consumption=10

if __name__ == "__main__" :
    #my_plane = Plane(200, weight=2000, cargo=50)
    #my_plane = Plane(200, cargo=50)
    #print(my_plane.fuel)
    #print(my_plane.max_cargo)
    #print(my_plane.cargo)
    #my_plane.cargo = 100
    #print(my_plane.cargo)
    #my_plane.load_cargo(100)
    #print(my_plane.cargo)
    #my_plane.load_cargo(100)
    #print(my_plane.cargo)

    #plane.remove_all_cargo())
    #print(my_plane.weight)
    #my_plane.weight = 3000
    #print(my_plane.weight)
    #plane.fuel)
    #plane.fuel_consumption)

    #my_plane.weight = 2000
    #print(my_plane.weight)

    from faker import Faker

    fake = Faker()

    weight = fake.pyint()
    print("weight=", weight)
    fuel = fake.pyint()
    #print("fuel=", fuel)
    fuel_consumption = fake.pyint()
    #print("fuel_consumption=", fuel_consumption)
    max_cargo = fake.pyint(1000, 50000)
    #print("max_cargo=", max_cargo)
    plane = Plane(weight, fuel, fuel_consumption, max_cargo)
    print("assigned weight =", plane.weight)

    assert plane.weight == weight








