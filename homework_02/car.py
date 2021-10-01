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
    engine = None
    def set_engine(self, engine) :
        #self.engine = Engine(volume, pistons)
        self.engine = engine

if __name__ == "__main__" :
    car = Car(0,0,0)
    #print(car.engine)
    #car.set_engine(1,2)
    #print(car.engine)
    #print(car.engine.volume)
    #print(car.engine.pistons)

    engine = Engine(100, 6)
    car.set_engine(engine)
    print(car.engine.volume)
    print(car.engine.pistons)




