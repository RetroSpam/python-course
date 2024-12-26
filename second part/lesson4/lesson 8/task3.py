products = {'Apple': 100, 'Banana': 80, 'Coffee': 250, 'Tea': 150}

cheapest_product = min(products, key=products.get)
most_expensive_product = max(products, key=products.get)

print(f"Cheapest product is {cheapest_product} at ₽{products[cheapest_product]}.")
print(f"Most expensive product is {most_expensive_product} at ₽{products[most_expensive_product]}.")
