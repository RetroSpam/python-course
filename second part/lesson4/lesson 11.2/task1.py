def sum_sales_with_for(sales):
    total = 0
    print("amount of purchase:", end=" ")
    
    for i, sale in enumerate(sales):
        total += sale
        if i < len(sales) - 1:
            print(sale, end="+")
        else:
            print(sale, end="=")
    
    print(total)

sum_sales_with_for([100, 200, 300])
sum_sales_with_for([15, 23, 39, 50])