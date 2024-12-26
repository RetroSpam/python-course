prices = {'Apple': 100, 'Banana': 80, 'Coffee': 250, 'Tea': 150}

def get_price(product_name):
    return prices.get(product_name, "Item not found")

item = input("Enter the name of the productAp: ")
price = get_price(item)
print(f"The price of {item} is: {price}")
