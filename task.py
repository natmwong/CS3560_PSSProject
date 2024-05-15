from datetime import datetime

class Task:

    # task_description can be one of the following: attending class, studying, working on assignment, etc.
    def __init__(self, start_date, start_time, duration, task_description, task_type):
        self.start_date = start_date
        self.start_time = start_time
        self.duration = duration
        self.task_description = task_description
        self.task_type = task_type

    def edit_task(self, new_start_date, new_start_time, new_duration, new_task_description, new_task_type):
        self.start_date = new_start_date
        self.start_time = new_start_time
        self.duration = new_duration
        self.task_description = new_task_description
        self.task_type = new_task_type