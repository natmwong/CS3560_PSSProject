class Model:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        # Add task to the list
        self.tasks.append(task)

    def edit_task(self, task):
        # Edit task in the list
        pass

    def delete_task(self, task):
        # Delete task from the list
        pass

    def validate_overlap(self, new_task):
        # Check for overlap with existing tasks
        pass