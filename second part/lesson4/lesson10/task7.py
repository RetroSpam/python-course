def calculate_discount(orders, index=0, previous_cost=None):
    if index >= len(orders):
        return []
    
    current_cost = orders[index]
    
    if previous_cost is not None:
        current_cost -= 0.1 * previous_cost
    

    return [round(current_cost)] + calculate_discount(orders, index + 1, orders[index])

orders1 = [1000, 2000, 3000]
orders2 = [5000, 10000, 15000]
orders3 = [100, 200, 300, 400]
orders4 = [50, 100]

print(calculate_discount(orders1))
print(calculate_discount(orders2))
print(calculate_discount(orders3))
print(calculate_discount(orders4)) 