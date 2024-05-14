from task import Task

class TransientTask(Task):

    # task_description can be one of the following: Visit, Shopping, and Appointment
    def __init__(self, start_time, duration, task_description):
        super().__init__(start_time, duration, task_description)