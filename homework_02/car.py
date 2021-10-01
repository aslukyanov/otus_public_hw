"""
создайте класс `Car`, наследник `Vehicle`

в модуле car создайте класс Car
класс Car должен быть наследником Vehicle
добавьте атрибут engine классу Car
объявите метод set_engine, который принимает в 
себя экземпляр объекта Engine и устанавливает 
на текущий экземпляр Car

"""
import sys
#print(sys.path)
sys.path.append('../')


from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle) :

    def set_engine(self, volume, pistons) :
        engine = Engine(volume, pistons)















