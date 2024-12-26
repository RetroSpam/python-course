def check_for_milk(products):
    if "Молоко" in products:
        return True
    else:
        return False


products1 = "Чай, Кофе, Сахар, Молоко, Мед"
products2 = "Яблоки, Груши, Бананы, Ананасы"


product_list1 = products1.split(", ")
product_list2 = products2.split(", ")


has_milk1 = check_for_milk(product_list1)
has_milk2 = check_for_milk(product_list2)


print(f"В товарах есть молоко: {has_milk1}")  # True
print(f"В товарах есть молоко: {has_milk2}")  # False
