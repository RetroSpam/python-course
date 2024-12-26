def update_employee_records(lines):
    supply_department = {}
    design_department = {}

    for line in lines:
        department, position, last_name = line.split(', ')
        if department == "Снабжение":
            supply_department[position] = last_name
        elif department == "Дизайн":
            design_department[position] = last_name

    return supply_department, design_department

# Input data
lines = [
    "Снабжение, Менеджер, Иванов",
    "Дизайн, Дизайнер, Смирнов",
    "Снабжение, Менеджер, Петров",
    "Дизайн, Иллюстратор, Сидоров",
    "Маркетинг, Аналитик, Сергеев",
    "Дизайн, Дизайнер, Васильев"
]

# Get the updated records
supply, design = update_employee_records(lines)

# Output the dictionaries
print("Снабжение:", supply)
print("Дизайн:", design)
