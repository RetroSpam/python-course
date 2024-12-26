def find_max_price(prices, index=0, current_max=None):
    if index == len(prices):
        return current_max
    
    if current_max is None or prices[index] > current_max:
        current_max = prices[index]
    
    return find_max_price(prices, index + 1, current_max)

print(find_max_price([15, 7, 9]))
print(find_max_price([1, 10, 20, 5]))
print(find_max_price([25, 25, 25]))
print(find_max_price([10, 8, 12]))