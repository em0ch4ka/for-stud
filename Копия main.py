1 Жеңіскүл
class Food:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self, _name):
        return self._name

    def get_price(self, _price):
        return self._price

    def set_name(self, _name):
        self._name = name

    def set_price(self, _price):
        self._price = price

    def description(self):
        pass


class FastFood(Food):
    def prepare_fastfood(self):
        return "Фастфуд тез дайындалады"

    def description(self):
        return self.prepare_fastfood()


class Drinks(Food):
    def pour_drink(self):
        return "Сусын құйылып жатыр"

    def description(self):
        return self.pour_drink()


class Dessert(Food):
    def bake_dessert(self):
        return "Десерт пісірілуде"

    def description(self):
        return self.bake_dessert()