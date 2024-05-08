from datetime import datetime, timedelta
from task import Task
from recurringTask import RecurringTask
from transientTask import TransientTask
from antiTask import AntiTask

class Model:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        # Add task to the list
        # Check for overlap before adding the task
        if self.validate_overlap(task):
            self.tasks.append(task)
            return True
        else:
            return False

    def edit_task(self, task, new_start_time, new_duration, new_task_type, **kwargs):
        if task in self.tasks:
            if isinstance(task, Task):
                # Call edit_task method of the Task class
                task.edit_task(new_start_time, new_duration, new_task_type)
            elif isinstance(task, RecurringTask):
                # Call edit_task method of the RecurringTask class
                task.edit_task(new_start_time, new_duration, new_task_type, **kwargs)
            elif isinstance(task, TransientTask):
                # Call edit_task method of the TransientTask class
                task.edit_task(new_start_time, new_duration, new_task_type)
            elif isinstance(task, AntiTask):
                # Call edit_task method of the AntiTask class
                task.edit_task(new_start_time, new_duration, new_task_type, **kwargs)

            return True
        else:
            return False

    def delete_task(self, task):
        # Delete task from the list
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        else:
            return False

    def validate_overlap(self, new_task):
        # Check for overlap with existing tasks
        new_start_time = datetime.strptime(new_task.start_time, "%I:%M %p")
        new_end_time = new_start_time + timedelta(minutes=new_task.duration)

        for task in self.tasks:
            task_start_time = datetime.strptime(task.start_time, "%I:%M %p")
            task_end_time = task_start_time + timedelta(minutes=task.duration)

            # Check if new task overlaps with existing task
            if (task_start_time <= new_start_time < task_end_time) or (new_start_time <= task_start_time < new_end_time):
                # Overlap detected
                return False
        
        # No overlap detected
        return True