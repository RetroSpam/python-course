products_input = "tea, coffee, sugar, honey"
position_to_remove = 2

products = products_input.split(", ")

products.pop(position_to_remove - 1)

print("products on the shelf:", ", ".join(products))
