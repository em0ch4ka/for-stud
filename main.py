1
Class Person: 
def__init__(_self,_name,_age):
   self.__name = name
   self.__age = age
def set_name(self.name):
    self.__name = name

def set_age(self,age):
    self.__age
def get_name(self):
    return self.__name

def get_age(self):
    return self.__age

P = Person() 

p.set_name("Жанель")
P.set_age(20)
print(p.get_name())
print(p.get_age())




Class Student(Person):
    def__init(self,name="",age=0, subject=""):
       super().__init__(name, age)