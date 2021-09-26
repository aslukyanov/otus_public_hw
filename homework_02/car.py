"""
создайте класс `Car`, наследник `Vehicle`

в модуле car создайте класс Car
класс Car должен быть наследником Vehicle
добавьте атрибут engine классу Car
объявите метод set_engine, который принимает в 
себя экземпляр объекта Engine и устанавливает 
на текущий экземпляр Car

"""

from base import Vehicle
from engine import Engine

class Car(Vehicle) :

    def set_engine(self, volume, pistons) :
        engine = Engine(volume, pistons)















