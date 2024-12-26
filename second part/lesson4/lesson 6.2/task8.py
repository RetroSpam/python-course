def swap_products(products, pos1, pos2):
   
    pos1 -= 1
    pos2 -= 1
    
    
    products[pos1], products[pos2] = products[pos2], products[pos1]
    return products

products = ["tea", "honey", "sugar"]
position1 = 1
position2 = 3

swapped_products = swap_products(products, position1, position2)
print("on the shelf:", ", ".join(swapped_products))
