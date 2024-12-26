def sort_objects(dict_list, key):
    return sorted(dict_list, key=lambda x: x[key])

data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_data = sort_objects(data, 'age')
print(sorted_data)