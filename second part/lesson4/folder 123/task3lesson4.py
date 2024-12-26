def convert_to_rubles(dollars, rate):
    return dollars * rate


rate = float(input("Enter the conversion rate (rubles per dollar): "))


prices_in_dollars = [1.2, 75, 10, 73.5]


for price in prices_in_dollars:
    price_in_rubles = convert_to_rubles(price, rate)
    print(f"{price_in_rubles:.1f}")
