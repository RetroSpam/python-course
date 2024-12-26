def check_order(order):
    """
    Checks if the order has items.
    
    Parameters:
    order (dict): The order dictionary containing 'id' and 'items'.
    
    Returns:
    dict: The order dictionary with an additional 'status' key.
    """
    if order['items']:
        order['status'] = 'ready'
    else:
        order['status'] = 'empty'
    return order

def package_order(order):

    if order['status'] == 'ready':
        return f"Dispatch: Order {order['id']} packed"
    else:
        return f"Dispatch: Order {order['id']} is empty"

def send_order(check_order_func, package_order_func, order):
   
    checked_order = check_order_func(order)
    return package_order_func(checked_order)

# Example usage
order1 = {'id': 1, 'items': ['book', 'pen']}
order2 = {'id': 2, 'items': []}

print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))