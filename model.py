from datetime import datetime, timedelta
from task import Task
from recurringTask import RecurringTask
from transientTask import TransientTask
from antiTask import AntiTask

class Model:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        # Check for overlap before adding the task
        if self.validate_overlap(task):
            if task.task_type == "Antitask":
                # Find the recurring task with the same start time
                for i, existing_task in enumerate(self.tasks):
                    if existing_task.task_type == "Recurring Task" and existing_task.start_date == task.start_date:
                        # Replace the recurring task with the anti-task
                        self.tasks[i] = AntiTask(task.start_date, task.start_time, task.duration, task.task_description, task.task_type)
                        return True  # Anti-task successfully replaced recurring task
                # If no recurring task is found, task is invalid
                return False
            else:
                # Add task to the list
                self.tasks.append(task)
                return True
        else:
            return False

    def edit_task(self, task, new_start_date, new_duration, new_task_type, **kwargs):
        if task in self.tasks:
            if isinstance(task, Task):
                # Call edit_task method of the Task class
                task.edit_task(new_start_date, new_duration, new_task_type)
            elif isinstance(task, RecurringTask):
                # Call edit_task method of the RecurringTask class
                task.edit_task(new_start_date, new_duration, new_task_type, **kwargs)
            elif isinstance(task, TransientTask):
                # Call edit_task method of the TransientTask class
                task.edit_task(new_start_date, new_duration, new_task_type)
            elif isinstance(task, AntiTask):
                # Call edit_task method of the AntiTask class
                task.edit_task(new_start_date, new_duration, new_task_type, **kwargs)

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
        new_start_time = datetime.strptime(new_task.start_time, "%H:%M")
        new_end_time = new_start_time + timedelta(minutes=new_task.duration)

        for task in self.tasks:
            task_start_time = datetime.strptime(task.start_time, "%H:%M")
            task_end_time = task_start_time + timedelta(minutes=task.duration)
            # Check if new task overlaps with existing task
            if (task_start_time <= new_start_time < task_end_time) or (new_start_time <= task_start_time < new_end_time):
                if new_task.task_type == "Antitask":
                    # Anti Task can overlap with any task
                    continue
                elif new_task.task_type == "Recurring Task":
                    continue
                elif new_task.start_date != task.start_date:
                    # Tasks have different start dates, no overlap
                    continue
                # Overlap detected
                return False
        return True
    
    def save_tasks_to_file(self, filename):
        # Save tasks to a file
        with open(filename, 'w') as file:
            for task in self.tasks:
                if isinstance(task, RecurringTask):
                    file.write(f"{task.start_date},{task.duration},{task.task_type},{task.recurrence_pattern},{task.start_date},{task.end_date}\n")
                elif isinstance(task, TransientTask):
                    file.write(f"{task.start_date},{task.duration},{task.task_type}\n")
                elif isinstance(task, AntiTask):
                    file.write(f"{task.start_date},{task.duration},{task.task_type},{task.referenced_task}\n")
                else:
                    file.write(f"{task.start_date},{task.duration},{task.task_type}\n")

    def load_tasks_from_file(self, filename):
        # Load tasks from a file
        with open(filename, 'r') as file:
            for line in file:
                task_data = line.strip().split(',')
                if len(task_data) == 3:
                    task = TransientTask(task_data[0], int(task_data[1]), task_data[2])
                elif len(task_data) == 4:
                    task = AntiTask(task_data[0], int(task_data[1]), task_data[2], task_data[3])
                elif len(task_data) == 6:
                    task = RecurringTask(task_data[0], int(task_data[1]), task_data[2], task_data[3], task_data[4], task_data[5])
                self.add_task(task)

    def get_all_tasks(self):
        return self.tasks