#5 нұсқа 1 бақылау
class Food:
    def_init_(self,name,price):
        self._name = _name
        self.price = _price

    def get_name(self,name):
        return self._name

    def get._price(self,price):
        return self._price

    def set_name(self,name):
        self._name = _name
   
    def set_price(self,price):
        self._price = price

    def work(self):
    print(self._name +"sale"


class Pizza(Food):
    def bake(self):
        print("Пицца пеште пісіріледі")
    
    def work(self):
        self.bake()

class Soup(Food):
    def cook(self):
        print("Сорпа қайнатылады")
    
    def work(self):
        self.cook()


class Dessert (Food):
    def decorate(self):
        print("Десерт безендіріледі")
    
    def work(self):
        self.decorate()

list = [Food("Margaritta","1500"),Soup("Borsh","1900"),Desert("Napalion","1300")]

for a in list:
   a.work()