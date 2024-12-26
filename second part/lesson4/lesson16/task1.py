def create_shelves():
    num_shelves = int(input("Enter number of shelves: "))
    shelf_lengths = list(map(int, input("Enter shelf lengths: ").split(','))) 
    shelves = [[length, 0] for length in shelf_lengths]
    print("Shelves:", shelves)
create_shelves()