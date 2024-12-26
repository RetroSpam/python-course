def find_element(lst, value):
    for element in lst:
        if element == value:
            return True
    return False

print(find_element([1, 2, 3, 4], 3))
print(find_element(['apple', 'banana', 'cherry'], 'orange'))