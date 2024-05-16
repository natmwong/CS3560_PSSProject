from task import Task
from recurringTask import RecurringTask
from transientTask import TransientTask
from antiTask import AntiTask

class Controller:
    def __init__(self, model):
        self.model = model

    # Add a task to the model
    def add_task(self, start_date, start_time, end_date, task_description, task_duration, task_type, recurrence_pattern):
        # Round task_duration to the nearest 15 minutes
        task_duration = round(int(task_duration) / 15) * 15

        if task_type == "Transient Task":
            task = TransientTask(start_date, start_time, task_duration, task_description, task_type)
            is_valid = self.model.add_task(task)
        elif task_type == "Recurring Task":
            task = RecurringTask(start_date, start_time, task_duration, task_description, task_type, recurrence_pattern, end_date)
            recurringTasks = task.generate_instances()
            for recurringTask in recurringTasks:
                is_valid = self.model.add_task(recurringTask)
                print(recurringTask)
        else:
            task = AntiTask(start_date, start_time, task_duration, task_description, task_type)
            is_valid = self.model.add_task(task)

        for task in self.model.tasks:
            print(task.task_description, task.start_date, task.start_time, task.duration, task.task_type)
        
        return is_valid
    def edit_task(self, task, updated_description, updated_time, updated_duration):
        # Find the task in the model and update its attributes
        task.task_description = updated_description
        task.start_time = updated_time
        task.duration = updated_duration
