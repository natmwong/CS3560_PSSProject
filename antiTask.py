from task import Task

class AntiTask(Task):

    # referenced_task is the recurring task that the anti-task is associated with
    # anti-task will replace one instance of a recurring task
    def __init__(self, start_time, duration, task_type, referenced_task):
        super().__init__(start_time, duration, task_type)
        self.referenced_task = referenced_task

    def edit_task(self, new_start_time, new_duration, new_task_type, new_referenced_task):
        super().edit_task(new_start_time, new_duration, new_task_type)
        self.referenced_task = new_referenced_task