def filter_odd_prices(prices):

    non_discounted_prices = [price for price in prices if price % 2 == 0]
    return non_discounted_prices

input_data = [
    [50, 45, 30, 25],
    [100, 90, 85, 70, 60]
]

for prices in input_data:
    non_discount_prices = filter_odd_prices(prices)
    print("prices without discount:", ', '.join(map(str, non_discount_prices)))
