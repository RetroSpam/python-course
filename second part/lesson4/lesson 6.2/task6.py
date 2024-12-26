
products_input = " tea, coffee, sugar"
position = 2
new_product = "honey"

products_list = products_input.split(", ")

products_list.insert(position - 1, new_product)  

result = ", ".join(products_list)

print("products on the shelf:", result)
