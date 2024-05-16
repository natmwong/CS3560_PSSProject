from task import Task

class TransientTask(Task):

    # task_description can be one of the following: Visit, Shopping, and Appointment
    def __init__(self, start_date, start_time, duration, task_description, task_type):
        super().__init__(start_date, start_time, duration, task_description, task_type)