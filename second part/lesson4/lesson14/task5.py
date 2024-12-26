def categorize_products(products):

    product_count = {}
    
    for product, category in products:
    
        product_count[category] = product_count.get(category, 0) + 1
    
    return product_count

input_data_1 = [('Shirt', 'Clothes'), ('Mug', 'Dishes')]
input_data_2 = [('Shirt', 'Clothes'), ('Pants', 'Clothes'), ('Mug', 'Dishes')]
input_data_3 = [('Pen', 'Stationery'), ('Notebook', 'Stationery'), ('Mug', 'Dishes'), ('Chair', 'Furniture')]

print(categorize_products(input_data_1))
print(categorize_products(input_data_2))
print(categorize_products(input_data_3))