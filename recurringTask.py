from task import Task
from datetime import datetime, timedelta

class RecurringTask(Task):

    # task_description can be one of the following: Course, Study, Sleep, Exercise, Work, and Meal
    # recurrence_pattern can be one of the following: Daily, Weekly, Monthly, and Yearly
    def __init__(self, start_date, start_time, duration, task_description, task_type, recurrence_pattern, end_date):
        super().__init__(start_date, start_time, duration, task_description, task_type)
        self.recurrence_pattern = recurrence_pattern
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")

    def generate_instances(self):
        instances = []
        current_date = datetime.strptime(self.start_date, "%Y-%m-%d")
        start_time = datetime.strptime(self.start_time, "%H:%M")
        while current_date <= self.end_date:
            if self.recurrence_pattern == "Weekly":
                if current_date.weekday() == datetime.strptime(self.start_date, "%Y-%m-%d").weekday():
                    instance_start_date = current_date.strftime("%Y-%m-%d")  # Convert datetime to string
                    instances.append(Task(instance_start_date, start_time, self.duration, self.task_description, self.task_type))
            elif self.recurrence_pattern == "Daily":
                instance_start_date = current_date.strftime("%Y-%m-%d")  # Convert datetime to string
                instances.append(Task(instance_start_date, start_time, self.duration, self.task_description, self.task_type))
            elif self.recurrence_pattern == "Monthly":
                if current_date.day == datetime.strptime(self.start_date, "%Y-%m-%d").day:
                    instance_start_date = current_date.strftime("%Y-%m-%d")  # Convert datetime to string
                    instances.append(Task(instance_start_date, start_time, self.duration, self.task_description, self.task_type))
            elif self.recurrence_pattern == "Yearly":
                if current_date.month == datetime.strptime(self.start_date, "%Y-%m-%d").month and current_date.day == datetime.strptime(self.start_date, "%Y-%m-%d").day:
                    instance_start_date = current_date.strftime("%Y-%m-%d")  # Convert datetime to string
                    instances.append(Task(instance_start_date, start_time, self.duration, self.task_description, self.task_type))
            current_date += timedelta(days=1)
            if current_date > self.end_date:  # Check if current_date exceeds the end_date
                break  # Exit the loop if current_date exceeds the end_date
        return instances


    # Override methods
    def edit_task(self, new_start_date, new_start_time, new_duration, new_task_description, new_recurrence_pattern, new_end_date):
        super().edit_task(new_start_date, new_start_time, new_duration, new_task_description)
        self.recurrence_pattern = new_recurrence_pattern
        self.start_date = new_start_date
        self.end_date = new_end_date