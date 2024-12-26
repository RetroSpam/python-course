def update_shelves():
    shelf_lengths = list(map(int, input("Shelves: ").split(',')))
    products = list(map(int, input("Number of products: ").split(',')))
    shelves = [[length, products[i]] for i, length in enumerate(shelf_lengths)]
    print("Shelves:", shelves)
update_shelves()