from task import Task
from recurringTask import RecurringTask
from transientTask import TransientTask
from antiTask import AntiTask

class Controller:
    def __init__(self, model):
        self.model = model

    # Add a task to the model
    def add_task(self, start_date, end_date, task_description, task_duration, task_type, recurrence_pattern):
        if task_type == "Transient Task":
            task = TransientTask(start_date, task_duration, task_description)
            self.model.add_task(task)
        elif task_type == "Recurring Task":
            task = RecurringTask(start_date, task_duration, task_description, recurrence_pattern, end_date)
            recurringTasks = task.generate_instances()
            for recurringTask in recurringTasks:
                self.model.add_task(recurringTask)
                print(recurringTask)
        else:
            task = AntiTask(start_date, task_duration, task_description)
            self.model.add_task(task)

        for task in self.model.tasks:
            print(task.task_description, task.start_time, task.duration)