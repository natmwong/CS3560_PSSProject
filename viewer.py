import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import Calendar
from functools import partial

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

        # Task Type Dropdown Menu
        ttk.Label(self.task_input_frame, text="Task Type:").grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.task_type_var = tk.StringVar(self.task_input_frame)
        task_types = ["Transient Task", "Transient Task", "Recurring Task", "Antitask"]
        # Set the default value for the dropdown menu
        self.task_type_var.set(task_types[0])
        self.task_type_dropdown = ttk.OptionMenu(self.task_input_frame, self.task_type_var, *task_types,  command=self.show_recurring_options)
        self.task_type_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Task Description Entry Field
        ttk.Label(self.task_input_frame, text="Task Description:").grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.task_description_entry = ttk.Entry(self.task_input_frame)
        self.task_description_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Duration Entry Field
        ttk.Label(self.task_input_frame, text="Duration (Minutes):").grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.duration_entry = ttk.Entry(self.task_input_frame)
        self.duration_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Recurrence Pattern Radio Buttons (Initially hidden)
        self.recurrence_pattern_var = tk.StringVar()
        self.recurrence_pattern_var.set("Daily")  # Default value
        self.recurrence_pattern_frame = ttk.Frame(self.task_input_frame)

        ttk.Label(self.recurrence_pattern_frame, text="Recurrence Pattern:").pack(side="left", padx=5, pady=5)
        for pattern in ["Daily", "Weekly", "Monthly", "Yearly"]:
            ttk.Radiobutton(self.recurrence_pattern_frame, text=pattern, variable=self.recurrence_pattern_var, value=pattern).pack(side="left", padx=5, pady=5)

        # Start Date Calendar Selector
        self.start_date_label = ttk.Label(self.task_input_frame, text="Start Date:")
        self.start_date_label.grid(row=4, column=0, padx=5, pady=5)
        self.start_date_calendar = Calendar(self.task_input_frame, selectmode="day", date_pattern="yyyy-mm-dd")
        self.start_date_calendar.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        # End Date Label (Initially hidden)
        self.end_date_label = ttk.Label(self.task_input_frame, text="End Date:")

        # End Date Calendar Selector (Initially hidden)
        self.end_date_calendar = Calendar(self.task_input_frame, selectmode="day", date_pattern="yyyy-mm-dd")

        # Button to add task
        self.add_button = ttk.Button(self.task_input_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=6, columnspan=2, padx=5, pady=10)

    def show_recurring_options(self, task_type):
        # Show recurrence pattern options if task type is "Recurring Task"
        if task_type == "Recurring Task":
            self.recurrence_pattern_frame.grid(row=4, columnspan=2, padx=5, pady=5, sticky="ew")
            self.start_date_label.grid(row=5, column=0, padx=5, pady=5)
            self.start_date_calendar.grid(row=5, column=1, padx=5, pady=5)
            self.end_date_label.grid(row=5, column=2, padx=5, pady=5)
            self.end_date_calendar.grid(row=5, column=3, padx=5, pady=5)
            self.add_button.grid(row=6, columnspan=2, padx=5, pady=10)
        else:
            self.start_date_label.grid(row=4, column=0, padx=5, pady=5)
            self.start_date_calendar.grid(row=4, column=1, padx=5, pady=5)
            self.recurrence_pattern_frame.grid_remove()
            self.end_date_calendar.grid_remove()
            self.end_date_label.grid_remove()

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
        start_date = self.start_date_calendar.get_date()
        end_date = self.end_date_calendar.get_date()
        task_description = self.task_description_entry.get()
        task_duration = self.duration_entry.get()
        task_type = self.task_type_var.get()
        recurrence_pattern = self.recurrence_pattern_var.get()

        # Call controller method to add the task
        self.controller.add_task(start_date, end_date, task_description, task_duration, task_type, recurrence_pattern)

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
            self.calendar.calevent_create(start_time, duration=task.duration, text=task.task_description, tags=task.task_type)

    def run(self):
        # Run the Tkinter main loop
        self.root.mainloop()