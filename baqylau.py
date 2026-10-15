print("5 Nuska")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self, name):
        self.name = name

    def accept_order(self, product):
        print(f"{self.name} дүкені тапсырысты қабылдады.")
        print(f"тауар: {product.name}")
        print(f"бағасы: {product.price} тенге")

product1 = Product("ноутбук", 250000)

shop1 = Shop("Tech Shop")
shop2 = Shop("Digital Shop")

shop1.accept_order(product1)
shop2.accept_order(product1)



























