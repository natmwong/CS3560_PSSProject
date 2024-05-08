from task import Task

class TransientTask(Task):
    def __init__(self, start_time, duration, task_type):
        super().__init__(start_time, duration, task_type)

    # Override methods as needed