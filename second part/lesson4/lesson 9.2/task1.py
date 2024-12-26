def calculate_discount(prices_and_discount):
    
    discount_percentage = prices_and_discount[-1]
    prices = prices_and_discount[:-1]
    
    total_discount = sum(price * discount_percentage / 100 for price in prices)
    
    return total_discount

print(calculate_discount([100, 200, 300, 10]))
print(calculate_discount([50, 150, 250, 20]))