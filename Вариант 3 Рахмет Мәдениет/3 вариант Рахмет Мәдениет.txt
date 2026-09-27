Рахмет Мәдениет вариант 3

class Appliance:
    def __init__(self, brand, power):
        self._brand = brand
        self._power = power

    def get_brand(self):
        return self._brand

    def get_power(self):
        return self._power

    def set_brand(self, brand):
        self._brand = brand

    def set_power(self, power):
        self._power = power

    def operate(self):
        print(self._brand + " құрылғысы жұмыс істеп тұр.")


class WashingMachine(Appliance):
    def wash(self):
        print("Кір жуғыш машина жуылады")

    def operate(self):
        self.wash()


class Refrigerator(Appliance):
    def cool(self):
        print("Тоңазытқыш салқындатады")

    def operate(self):
        self.cool()


class Microwave(Appliance):
    def heat(self):
        print("Микротолқынды пеш тағамды қыздырады")

    def operate(self):
        self.heat()


appliances = [
    WashingMachine("LG", 500),
    Refrigerator("Samsung", 300),
    Microwave("Bosch", 800)
]

for a in appliances:
    a.operate()