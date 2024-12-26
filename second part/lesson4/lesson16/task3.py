def generate_discounts(shelves):
    discounts = []
    for index, shelf in enumerate(shelves):
        shelf_length, num_products = shelf
        discount_value = (index + 1) * num_products
        discounts.append([discount_value] * num_products)
    print("Discounts:", discounts)
shelves_1 = [[4, 2], [5, 3], [6, 5]]
generate_discounts(shelves_1)

shelves_2 = [[3, 1], [4, 4]]
generate_discounts(shelves_2)