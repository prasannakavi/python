from abc import ABC,abstractmethod
class car(ABC):
   def __init__(self,name,color,price,):
    self.name=name
    self.color=color
    self.price=price
    self.speed=0
   @abstractmethod
   def stop():
       pass
   @abstractmethod
   def speed_up(self):
       pass
   @abstractmethod
   def speed_down(self):
       pass
class Bmw(car):
    def speed_up(self):  
        self.speed+=5
    def speed_down(self):
        self.speed=-5
    def stop(self):
        self.stop=0
Bmw1=Bmw('x7','black',50000,)    
