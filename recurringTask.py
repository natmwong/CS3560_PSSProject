from task import Task
from datetime import datetime, timedelta

class RecurringTask(Task):

    # task_type can be one of the following: Course, Study, Sleep, Exercise, Work, and Meal
    # recurrence_pattern can be one of the following: Daily, Weekly, Monthly, and Yearly
    def __init__(self, start_time, duration, task_type, recurrence_pattern, start_date, end_date):
        super().__init__(start_time, duration, task_type)
        self.recurrence_pattern = recurrence_pattern
        self.start_date = start_date
        self.end_date = end_date

    # Generate instances of the recurring task based on the recurrence pattern
    def generate_instances(self):
        instances = []
        current_date = self.start_date
        while current_date <= self.end_date:
            if self.recurrence_pattern == "Weekly":
                if current_date.weekday() == self.start_date.weekday():
                    instance_start_time = datetime.combine(current_date, datetime.strptime(self.start_time, "%I:%M %p").time())
                    instances.append(Task(instance_start_time, self.duration, self.task_type))
            elif self.recurrence_pattern == "Daily":
                instance_start_time = datetime.combine(current_date, datetime.strptime(self.start_time, "%I:%M %p").time())
                instances.append(Task(instance_start_time, self.duration, self.task_type))
            elif self.recurrence_pattern == "Monthly":
                if current_date.day == self.start_date.day:
                    instance_start_time = datetime.combine(current_date, datetime.strptime(self.start_time, "%I:%M %p").time())
                    instances.append(Task(instance_start_time, self.duration, self.task_type))
            elif self.recurrence_pattern == "Yearly":
                if current_date.month == self.start_date.month and current_date.day == self.start_date.day:
                    instance_start_time = datetime.combine(current_date, datetime.strptime(self.start_time, "%I:%M %p").time())
                    instances.append(Task(instance_start_time, self.duration, self.task_type))
            current_date += timedelta(days=1)
        return instances

    # Override methods
    def edit_task(self, new_start_time, new_duration, new_task_type, new_recurrence_pattern, new_start_date, new_end_date):
        super().edit_task(new_start_time, new_duration, new_task_type)
        self.recurrence_pattern = new_recurrence_pattern
        self.start_date = new_start_date
        self.end_date = new_end_date

    def validate(self):
        # Call the validate method of the parent class (Task)
        if not super().validate():
            return False

        # Validate specific attributes of RecurringTask
        # Ensure recurrence pattern, start date, and end date are valid
        if not self.recurrence_pattern or not self.start_date or not self.end_date:
            return False
        
        return True