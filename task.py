class Task:

    # task_description can be one of the following: attending class, studying, working on assignment, etc.
    def __init__(self, start_time, duration, task_description, task_type):
        self.start_time = start_time
        self.duration = duration
        self.task_description = task_description
        self.task_type = task_type

    def validate(self):
        # Ensure start time is in valid format
        # Ensure duration is a positive integer or time format
        if not self.start_time:
            return False
        if not self.duration:
            return False
        
        return True

    def edit_task(self, new_start_time, new_duration, new_task_description):
        self.start_time = new_start_time
        self.duration = new_duration
        self.task_description = new_task_description