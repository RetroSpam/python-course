def log_price_change(func):
    def wrapper(item, old_price, new_price):
        result = func(item, old_price, new_price)
        print(f"price for {item} changed! {old_price} > {new_price}")
        return result
    return wrapper

@log_price_change
def change_price(item, old_price, new_price):
    pass

change_price('Chair', 5000, 4500)
change_price('Table', 8000, 7600)