import json

def check_inventory(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    items_to_purchase = []
    
    for item in data['inventory']:
        if item['quantity'] < item['minimum_required']:
            amount_needed = item['minimum_required'] - item['quantity']
            items_to_purchase.append(f"{item['item']} {amount_needed} pcs.")
    
    if items_to_purchase:
        print("You need to purchase:")
        for item in items_to_purchase:
            print(item)
    else:
        print("No items need to be purchased.")

check_inventory('inventory.json')