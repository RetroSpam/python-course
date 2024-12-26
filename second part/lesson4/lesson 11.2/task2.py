def count_specific_items_with_while(items, category):
    count = 0
    index = 0
    while index < len(items):
        if items[index] == category:
            count += 1
        index += 1
    return count

# Example usage:
items1 = ['fruit', 'toy', 'fruit', 'toy']
category1 = 'toy'
print(f"quantity '{category1}': {count_specific_items_with_while(items1, category1)}")

items2 = ['clothes', 'clothes', 'clothes']
category2 = 'clothes'
print(f"quantity '{category2}': {count_specific_items_with_while(items2, category2)}")