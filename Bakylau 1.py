вариант 7

class Computer:
    def __init__(self, _model, _year):
        self._model = _model
        self._year = _year
    
    
    def get_model(self, _model):
    	return self._model

    def get_year(self, _year):
    	return self._year

    def set_model(self, _model):
    	self._model = _model
   
    def set_year(self, _year):
	    self._year = _year
    
    def work(self):
	    print(self._model + "sdf")


class Desktop(Computer):
    def start(self):
        print("Үстел компьютерді іске қосады")

    def work(self):
	    self.start()

class GamingPC(Computer):
    def play_game(self):
	    print("Ойын компьтері ойынды іске қосады")

    def work(self):
	    self.play_game()

class Server(Computer):
    def process_data(self):
	    print("Сервер деректерді өндейді")

    def work(self):
	    self.process_data()

list = [Computer("fff","55"), Desktop("log","15"), GamingPC("ASUS","200"), Server("PC","55")]


for a in list:
    a.work()