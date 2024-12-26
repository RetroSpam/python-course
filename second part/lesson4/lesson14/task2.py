def round_to_nearest_hundred(prices):
    rounded_prices = list(map(lambda x: round(x / 100) * 100, prices))
    return rounded_prices

prices = [99, 150, 200, 349, 501]
rounded_prices = round_to_nearest_hundred(prices)
print(rounded_prices)