class Task:

    # task_type can be one of the following: attending class, studying, working on assignment, etc.
    def __init__(self, start_time, duration, task_type):
        self.start_time = start_time
        self.duration = duration
        self.task_type = task_type

    def validate(self):
        # Ensure start time is in valid format
        # Ensure duration is a positive integer or time format
        if not self.start_time:
            return False
        if not self.duration:
            return False
        
        return True

    def create(self):
        # Add creation logic here
        pass

    def edit_task(self, new_start_time, new_duration, new_task_type):
        self.start_time = new_start_time
        self.duration = new_duration
        self.task_type = new_task_type