def track_low_stock_with_for(products, threshold):
    print("low stock:")
    for product, quantity in products.items():
        if quantity < threshold:
            print(f"{product} - {quantity}")


products = {'apples': 50, 'bananas': 10, 'cherries': 3}
threshold = 15
track_low_stock_with_for(products, threshold)