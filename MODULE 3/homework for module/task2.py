from datetime import datetime

class Product:
    def __init__(self, name, price, date_of_purchase):
        self.name = name
        self.price = price
        self.date_of_purchase = date_of_purchase

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, date_of_purchase={self.date_of_purchase})"

class Customer:
    def __init__(self, first_name, last_name, date_of_birth, id_card, visitor_info):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.id_card = id_card
        self.visitor_info = visitor_info
        self.purchased_products = []

    def add_product(self, product):
        self.purchased_products.append(product)

    def __repr__(self):
        return (f"Customer(first_name={self.first_name}, last_name={self.last_name}, "
                f"date_of_birth={self.date_of_birth}, id_card={self.id_card}, "
                f"visitor_info={self.visitor_info}, purchased_products={self.purchased_products})")

# Example usage
customer = Customer("Hassan", "Al-hakkak", "1995-07-26", "ID123456", "Regular visitor")
product1 = Product("Laptop", 1200.00, datetime.now().strftime("%Y-%m-%d"))
product2 = Product("Smartphone", 800.00, datetime.now().strftime("%Y-%m-%d"))

customer.add_product(product1)
customer.add_product(product2)

print(customer)