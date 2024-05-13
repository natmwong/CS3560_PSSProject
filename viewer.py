import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import Calendar

class Viewer:
    def __init__(self, controller, model):
        self.controller = controller
        self.model = model

        # Initialize Tkinter window
        self.root = tk.Tk()
        self.root.title("Personal Scheduling System")

        # Create input fields for task creation
        self.create_task_input()

        # Create calendar view for displaying schedule
        self.create_calendar_view()

    def create_task_input(self):
        # Frame for task input fields
        self.task_input_frame = ttk.Frame(self.root)
        self.task_input_frame.pack(pady=10)

        # Start Time Calendar Selector
        ttk.Label(self.task_input_frame, text="Start Time:").grid(row=0, column=0, padx=5, pady=5)
        self.start_time_calendar = Calendar(self.task_input_frame, selectmode="day", date_pattern="yyyy-mm-dd")
        self.start_time_calendar.grid(row=0, column=1, padx=5, pady=5)

        # Duration Entry Field (Only for Hours)
        ttk.Label(self.task_input_frame, text="Duration (Hours):").grid(row=1, column=0, padx=5, pady=5)
        self.duration_entry = ttk.Entry(self.task_input_frame)
        self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

        # Task Type Dropdown Menu
        ttk.Label(self.task_input_frame, text="Task Type:").grid(row=2, column=0, padx=5, pady=5)
        self.task_type_var = tk.StringVar(self.task_input_frame)
        task_types = ["Transient", "Recurring", "Anti"]
        self.task_type_dropdown = ttk.OptionMenu(self.task_input_frame, self.task_type_var, *task_types)
        self.task_type_dropdown.grid(row=2, column=1, padx=5, pady=5)

        # Button to add task
        add_button = ttk.Button(self.task_input_frame, text="Add Task", command=self.add_task)
        add_button.grid(row=3, columnspan=2, padx=5, pady=10)

    def create_calendar_view(self):
        # Frame for calendar view
        self.calendar_frame = ttk.Frame(self.root)
        self.calendar_frame.pack(pady=10)

        # Button to display schedule
        display_schedule_button = ttk.Button(self.calendar_frame, text="Display Schedule", command=self.display_schedule)
        display_schedule_button.pack(pady=5)

        # Calendar widget for displaying the schedule
        self.calendar = Calendar(self.calendar_frame, selectmode='none')
        self.calendar.pack(padx=10, pady=5)

    def add_task(self):
        # Get task details from input fields
        start_time = self.start_time_entry.get()
        duration = self.duration_entry.get()
        task_type = self.task_type_entry.get()

        # Call controller method to add the task
        self.controller.add_task(start_time, duration, task_type)

    def display_schedule(self):
        # Clear existing calendar
        self.calendar.delete('all')

        # Get all tasks from the model
        tasks = self.model.get_all_tasks()

        # Display tasks on the calendar
        for task in tasks:
            # Convert start time to datetime object
            start_time = datetime.strptime(task.start_time, "%Y-%m-%d %H:%M:%S")

            # Add task details to the calendar
            self.calendar.calevent_create(start_time, duration=task.duration, text=task.task_type)

    def run(self):
        # Run the Tkinter main loop
        self.root.mainloop()