def binary_find_element(sorted_list, element):
    left = 0
    right = len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == element:
            return True
        elif sorted_list[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

print(binary_find_element([], 3))
print(binary_find_element([1, 2, 3, 4, 5], 3))
print(binary_find_element([1, 2, 3, 4, 5], 6))