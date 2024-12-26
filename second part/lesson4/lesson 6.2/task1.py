
def display_odd_index_products(product_list):
    products = product_list.split(", ")
    
    odd_index_products = [products[i] for i in range(1, len(products), 2)]
    
    result = ", ".join(odd_index_products)
    
    return result

input1 = "Чай, Кофе, Сахар, Молоко, Мед"
input2 = "Яблоки, Груши, Бананы, Ананасы"

output1 = display_odd_index_products(input1)
output2 = display_odd_index_products(input2)

print(f"Товары с нечетными индексами: {output1}")
print(f"Товары с нечетными индексами: {output2}")
