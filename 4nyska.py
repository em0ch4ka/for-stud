class OperatingSystem:
    def run_program(self):
        print("Операционная система жұмысын бастады")


class Computer:
    def __init__(self, computer):  
        self.computer = computer
        self.operatingsystem = OperatingSystem()

    def run_program(self):  
        print(f"Компьютер: {self.computer}")
        self.operatingsystem.run_program()


PC = Computer("Legion PC")
PC.run_program()


class Player:
    def __init__(self, health, level):
        self.__health = health 
        self._level = level

    def display_info(self):
        print(f"Уровень здоровья: {self.__health}, Уровень: {self._level}")


class Wizard:  
    def attack_as_wizard(self):
        print("Магическая атака!")


class Warrior(Player):
    def __init__(self, health, level):
        super().__init__(health, level)

    def calculate_power(self): 
        base_power = self._level * 10
        return base_power * 5 

    def attack(self):
        power = self.calculate_power()
        print(f"Атакует с силой {power}")


class Hero(Wizard, Warrior):  
    def attack_as_warrior(self):
        Warrior.attack(self)


hero = Hero(100, 4)
hero.display_info()
hero.attack_as_warrior()