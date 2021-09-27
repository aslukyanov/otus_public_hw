"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle
import exceptions

class Plane(Vehicle) :
    def __init__(self, max_cargo, weight=1000, fuel=0, fuel_consumption=10, cargo=100) :
        super().__init__(weight=1000, fuel=0, fuel_consumption=10)
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
    my_plane = Plane(200, weight=2000, cargo=50)
    #print(my_plane.fuel)
    #print(my_plane.max_cargo)
    #print(my_plane.cargo)

    my_plane.load_cargo(100)
    #print(my_plane.cargo)
    #my_plane.load_cargo(100)
    #print(my_plane.cargo)

    print(my_plane.remove_all_cargo())
    print(my_plane.weight)
    print(my_plane.fuel)
    print(my_plane.fuel_consumption)

    my_plane.weight = 2000
    print(my_plane.weight)






