from task import Task

class RecurringTask(Task):

    # task_type can be one of the following: Course, Study, Sleep, Exercise, Work, and Meal
    # recurrence_pattern can be one of the following: Daily, Weekly, Monthly, and Yearly
    def __init__(self, start_time, duration, task_type, recurrence_pattern, start_date, end_date):
        super().__init__(start_time, duration, task_type)
        self.recurrence_pattern = recurrence_pattern
        self.start_date = start_date
        self.end_date = end_date

    # Override methods as needed
    def edit_task(self, new_start_time, new_duration, new_task_type, new_recurrence_pattern, new_start_date, new_end_date):
        super().edit_task(new_start_time, new_duration, new_task_type)
        self.recurrence_pattern = new_recurrence_pattern
        self.start_date = new_start_date
        self.end_date = new_end_date