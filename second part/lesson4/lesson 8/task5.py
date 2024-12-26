def unique_products(store1, store2):
    products_store1 = set(store1.split(','))
    products_store2 = set(store2.split(','))

    unique_to_store1 = products_store1 - products_store2
    unique_to_store2 = products_store2 - products_store1

    return list(unique_to_store1), list(unique_to_store2)

store1_input = "bread,milk,cheese,coffee,tea,sugar"
store2_input = "milk,yogurt,juice,cacao,tea,condenced milk"

unique_store1, unique_store2 = unique_products(store1_input, store2_input)
print("Unique to Store 1:", unique_store1)
print("Unique to Store 2:", unique_store2)
