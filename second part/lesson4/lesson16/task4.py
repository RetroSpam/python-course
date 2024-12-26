def create_sales_matrix():
    num_shelves = int(input("Enter number of shelves: "))
    
    sales_matrix = []
    
    for _ in range(num_shelves):
        sales_input = input("Sales by product: ")
        
        sales_data = list(map(int, sales_input.split(',')))
        
        sales_matrix.append(sales_data)
    
    print("Sales:", sales_matrix)

create_sales_matrix()