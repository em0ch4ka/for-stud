class OperatingSystem:



&#x20; def \_\_init\_\_(self, name: str):

&#x20;   self.name = name

&#x20; def start(self):

&#x20;   print(f"{self.name} операциялық жүйесі іске қосылуда...")





class Computer:



&#x20; def \_\_init\_\_(self, os\_name: str):

&#x20;   self.os = OperatingSystem(os\_name)



&#x20; def run\_program(self):

&#x20;   print("Компьютер іске қосылды.")

&#x20;   self.os.start()

&#x20;   print("Бағдарлама сәтті іске қосылды!")





comp = Computer("Windows 11")

comp.run\_program()

