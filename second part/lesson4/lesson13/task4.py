def estimate_time(project_name, number_of_tasks):
    if not isinstance(project_name, str):
        return "Error: First argument isn't a chain!"
    if not isinstance(number_of_tasks, int):
        return "Error: Second argument isnt a number!"
    
    return "Estimated time calculated successfully."

print(estimate_time('Веб-сайт', 'пять'))
print(estimate_time('Визитка', 10))