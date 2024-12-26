class Task:
    def __init__(self, date, name, description, tags):
        self.date = date
        self.name = name
        self.description = description
        self.tags = tags

class ToDoListBot:
    def __init__(self):
        self.tasks = []

    def add_task(self, date, name, description, tags):
        task = Task(date, name, description, tags)
        self.tasks.append(task)
        return f"Task '{name}' added successfully!"

    def view_tasks(self):
        return [vars(task) for task in self.tasks]

    def edit_task(self, task_name, **kwargs):
        for task in self.tasks:
            if task.name == task_name:
                for key, value in kwargs.items():
                    setattr(task, key, value)
                return f"Task '{task_name}' updated successfully!"
        return "Task not found."

    def delete_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]
        return f"Task '{task_name}' deleted successfully!"