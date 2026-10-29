1 - тапсырма.
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def register_student(self, student):
        self.students.append((student.name, student.student_id))
        print(f"{student.name} (ID: {student.student_id}) {self.name} университетінде тіркелді")

uni1, uni2 = University("КазНУ"), University("ЕНУ")
s = Student("Мади", 101)
uni1.register_student(s)
uni2.register_student(s)

2 - тапсырма.

class Payment:
    def __init__(self, amount, currency):
        self.__amount = amount
        self._currency = currency

    def get_amount(self):
        return self.__amount

    def display_info(self):
        print(f"Сома: {self.__amount} {self._currency}")

    def process_payment(self):
        return self.__amount

    def calculate_fee(self):
        return 0


class CashPayment(Payment):
    def calculate_fee(self):
        return 0

    def process_payment(self):
        return self.get_amount() * 5


class CardPayment(Payment):
    def calculate_fee(self):
        return self.get_amount() * 0.02

    def process_payment(self):
        return self.get_amount() / 5


class OnlinePayment(CashPayment, CardPayment):
    pass


p = OnlinePayment(1000, "KZT")
p.display_info()
print(p.process_payment())
print(CardPayment.process_payment(p))
print(p.calculate_fee())