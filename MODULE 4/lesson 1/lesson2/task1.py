import json

def calculate_revenue_by_category(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    revenue_by_category = {}
    
    for sale in data['sales']:
        category = sale['category']
        total_price = sale['total_price']
        
        if category in revenue_by_category:
            revenue_by_category[category] += total_price
        else:
            revenue_by_category[category] = total_price
    
    for category, revenue in revenue_by_category.items():
        print(f"Revenue by category \"{category}\": {revenue}")

calculate_revenue_by_category('sales.json')