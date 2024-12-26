def calculate_volume(books, stationery, toys):
    volume_books = books * 2  
    volume_stationery = stationery * 1.5  
    volume_toys = toys * 3 
    
    total_volume = volume_books + volume_stationery + volume_toys
    return total_volume


books = int(input("Enter the number of boxes of books: "))
stationery = int(input("Enter the number of boxes of stationery: "))
toys = int(input("Enter the number of boxes of toys: "))

total_volume = calculate_volume(books, stationery, toys)
print(f"The total volume required is: {total_volume} m³")
