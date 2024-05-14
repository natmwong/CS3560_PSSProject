from task import Task
from recurringTask import RecurringTask

class AntiTask(Task):

    # referenced_task is the recurring task that the anti-task is associated with
    # anti-task will replace one instance of a recurring task
    def __init__(self, start_time, duration, task_description):
        super().__init__(start_time, duration, task_description)

    # Replace the recurring task instance with the anti-task
    def replace_recurring_task_instance(self, model):
        # Get all recurring tasks from the model
        recurring_tasks = [task for task in model.tasks if isinstance(task, RecurringTask)]
        
        # Check for time conflicts and replace the first instance found
        for recurring_task in recurring_tasks:
            for instance in recurring_task.generate_instances():
                if instance.start_time == self.start_time:
                    # Replace the instance with the anti-task
                    instance.start_time = self.start_time
                    instance.duration = self.duration
                    instance.task_description = self.task_description
                    return 1  # Stop after replacing one instance
        return 0  # If no instances were replaced

    #Overide methods
    def edit_task(self, new_start_time, new_duration, new_task_type):
        super().edit_task(new_start_time, new_duration, new_task_type)