def most_responsible_employee(tasks_completed):
 return max(tasks_completed, key=lambda employee: tasks_completed[employee])

tasks_completed = {
    'Alice': 15,
    'Bob': 20,
    'Charlie': 18
}

most_responsible = most_responsible_employee(tasks_completed)
print(f"The most responsible employee is: {most_responsible}")