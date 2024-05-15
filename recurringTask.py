from task import Task
from datetime import datetime, timedelta

class RecurringTask(Task):

    # task_description can be one of the following: Course, Study, Sleep, Exercise, Work, and Meal
    # recurrence_pattern can be one of the following: Daily, Weekly, Monthly, and Yearly
    def __init__(self, start_time, duration, task_description, recurrence_pattern, end_date):
        super().__init__(start_time, duration, task_description)
        self.recurrence_pattern = recurrence_pattern
        self.end_date = end_date

    # Generate instances of the recurring task based on the recurrence pattern from start_time to end_date
    def generate_instances(self):
        instances = []
        current_date = self.start_time
        while current_date <= self.end_date:
            if self.recurrence_pattern == "Weekly":
                if current_date.weekday() == self.start_time.weekday():
                    instance_start_time = datetime.combine(current_date, datetime.strptime(self.start_time, "%I:%M %p").time())
                    instances.append(Task(instance_start_time, self.duration, self.task_description))
            elif self.recurrence_pattern == "Daily":
                instance_start_time = datetime.combine(current_date, datetime.strptime(self.start_time, "%I:%M %p").time())
                instances.append(Task(instance_start_time, self.duration, self.task_description))
            elif self.recurrence_pattern == "Monthly":
                if current_date.day == self.start_time.day:
                    instance_start_time = datetime.combine(current_date, datetime.strptime(self.start_time, "%I:%M %p").time())
                    instances.append(Task(instance_start_time, self.duration, self.task_description))
            elif self.recurrence_pattern == "Yearly":
                if current_date.month == self.start_time.month and current_date.day == self.start_time.day:
                    instance_start_time = datetime.combine(current_date, datetime.strptime(self.start_time, "%I:%M %p").time())
                    instances.append(Task(instance_start_time, self.duration, self.task_description))
            current_date += timedelta(days=1)
            if current_date > self.end_date:  # Check if current_date exceeds the end_date
                break  # Exit the loop if current_date exceeds the end_date
        return instances

    # Override methods
    def edit_task(self, new_start_time, new_duration, new_task_description, new_recurrence_pattern, new_end_date):
        super().edit_task(new_start_time, new_duration, new_task_description)
        self.recurrence_pattern = new_recurrence_pattern
        self.start_time = new_start_time
        self.end_date = new_end_date

    def validate(self):
        # Call the validate method of the parent class (Task)
        if not super().validate():
            return False

        # Validate specific attributes of RecurringTask
        # Ensure recurrence pattern, start date, and end date are valid
        if not self.recurrence_pattern or not self.end_date:
            return False
        
        return True