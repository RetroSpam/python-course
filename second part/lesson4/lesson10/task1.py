def calculate_final_cost(original_cost, visits):
    if visits >= 20:
        discount = 0.20
    elif visits >= 10:
        discount = 0.10
    else:
        discount = 0.0

    final_cost = original_cost * (1 - discount)
    return final_cost

# Test cases
print(calculate_final_cost(100, 5))
print(calculate_final_cost(200, 10))
print(calculate_final_cost(150, 20))