import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import Calendar
from functools import partial
from recurringTask import RecurringTask

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

        # Create "Display Schedule" button
        self.display_schedule_button = ttk.Button(self.root, text="Display Schedule", command=self.display_schedule)
        self.display_schedule_button.pack(pady=5)

    def create_task_input(self):
        # Frame for task input fields
        self.task_input_frame = ttk.Frame(self.root)
        self.task_input_frame.pack(pady=10)

        # Task Type Dropdown Menu
        ttk.Label(self.task_input_frame, text="Task Type:").grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.task_type_var = tk.StringVar(self.task_input_frame)
        task_types = ["Transient Task", "Transient Task", "Recurring Task", "Antitask"]
        self.task_type_var.set(task_types[0])
        self.task_type_dropdown = ttk.OptionMenu(self.task_input_frame, self.task_type_var, *task_types, command=self.show_recurring_options)
        self.task_type_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Task Description Entry Field
        ttk.Label(self.task_input_frame, text="Task Description:").grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.task_description_entry = ttk.Entry(self.task_input_frame)
        self.task_description_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Start Time Entry Field
        ttk.Label(self.task_input_frame, text="Start Time (HH:MM):").grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.start_time_entry = ttk.Entry(self.task_input_frame)
        self.start_time_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Duration Entry Field
        ttk.Label(self.task_input_frame, text="Duration (Minutes):").grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        self.duration_entry = ttk.Entry(self.task_input_frame)
        self.duration_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        # Recurrence Pattern Radio Buttons (Initially hidden)
        self.recurrence_pattern_var = tk.StringVar()
        self.recurrence_pattern_var.set("Daily")  # Default value
        self.recurrence_pattern_frame = ttk.Frame(self.task_input_frame)
        ttk.Label(self.recurrence_pattern_frame, text="Recurrence Pattern:").pack(side="left", padx=5, pady=5)
        for pattern in ["Daily", "Weekly", "Monthly", "Yearly"]:
            ttk.Radiobutton(self.recurrence_pattern_frame, text=pattern, variable=self.recurrence_pattern_var, value=pattern).pack(side="left", padx=5, pady=5)

        # Start Date Calendar Selector
        self.start_date_label = ttk.Label(self.task_input_frame, text="Start Date:")
        self.start_date_label.grid(row=5, column=0, padx=5, pady=5)
        self.start_date_calendar = Calendar(self.task_input_frame, selectmode="day", date_pattern="yyyy-mm-dd")
        self.start_date_calendar.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

        # End Date Label (Initially hidden)
        self.end_date_label = ttk.Label(self.task_input_frame, text="End Date:")
        # End Date Calendar Selector (Initially hidden)
        self.end_date_calendar = Calendar(self.task_input_frame, selectmode="day", date_pattern="yyyy-mm-dd")

        # Button to add task
        self.add_button = ttk.Button(self.task_input_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=7, columnspan=2, padx=5, pady=10)

    def update_task_type_var(self, *args):
        # Update task_type_var with the selected value from the option menu
        self.task_type_var.set(self.task_type_var.get())

    def show_recurring_options(self, task_type):
        # Show recurrence pattern options if task type is "Recurring Task"
        if task_type == "Recurring Task":
            self.recurrence_pattern_frame.grid(row=5, columnspan=2, padx=5, pady=5, sticky="ew")
            self.start_date_label.grid(row=6, column=0, padx=5, pady=5)
            self.start_date_calendar.grid(row=6, column=1, padx=5, pady=5)
            self.end_date_label.grid(row=6, column=2, padx=5, pady=5)
            self.end_date_calendar.grid(row=6, column=3, padx=5, pady=5)
            self.add_button.grid(row=7, columnspan=2, padx=5, pady=10)
            self.task_type_var.trace_add("write", self.update_task_type_var)
        else:
            self.start_date_label.grid(row=5, column=0, padx=5, pady=5)
            self.start_date_calendar.grid(row=5, column=1, padx=5, pady=5)
            self.recurrence_pattern_frame.grid_remove()
            self.end_date_calendar.grid_remove()
            self.end_date_label.grid_remove()

    def create_calendar_view(self):
        # Frame for calendar view
        self.calendar_frame = ttk.Frame(self.root)
        self.calendar_frame.pack(pady=10)

    def add_task(self):
        # Get task details from input fields
        self.task_type_var.trace_add("write", self.update_task_type_var)
        start_time = self.start_time_entry.get()
        start_date = self.start_date_calendar.get_date()
        end_date = self.end_date_calendar.get_date() if self.task_type_var.get() == "Recurring Task" else start_date
        task_description = self.task_description_entry.get()
        task_duration = self.duration_entry.get()
        print("Duration: " + task_duration)
        task_type = self.task_type_var.get()
        recurrence_pattern = self.recurrence_pattern_var.get()
        # Check if task description or task duration is empty
        if task_description == '' or task_duration == '' or start_time == '' or start_date == '' or (task_type == "Recurring Task" and end_date == ''):
            messagebox.showerror("Missing Information", "Please fill out all task information fields.")
        elif task_duration.isnumeric() == False:
            messagebox.showerror("Invalid Duration", "Duration must be a number in minutes.")
        elif not self.is_valid_time(start_time):
            messagebox.showerror("Invalid Time", "Start time must be in the format HH:MM.")
        else:
            # Call controller method to add the task
            is_valid = self.controller.add_task(start_date, start_time, end_date, task_description, task_duration, task_type, recurrence_pattern)
            if is_valid:
                messagebox.showinfo("Task Added", "Task added successfully.")
            elif task_type == "Antitask":
                messagebox.showerror("Task Error", "Antitasks may only replace Recurring Tasks. Please select a Recurring Task to replace.")
            else:
                messagebox.showerror("Task Conflict", "Task date conflicts with existing task. Please choose a different date or create an Antitask if existing task is Recurring.")
        print("Task added successfully")

    def is_valid_time(self, time_str):
        try:
            datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False

    def display_schedule(self):
        # Clear previous calendar if it exists
        if hasattr(self, 'calendar_frame'):
            self.calendar_frame.destroy()

        # Frame for calendar view
        self.calendar_frame = ttk.Frame(self.root)
        self.calendar_frame.pack(pady=10)

        # Calendar widget for displaying the schedule
        self.calendar = Calendar(self.calendar_frame, selectmode='day')
        self.calendar.pack(padx=10, pady=5)

        # Button to display task information
        self.task_info_button = ttk.Button(self.calendar_frame, text="Get Task Information", command=self.task_info)
        self.task_info_button.pack(pady=20)

        # Get all tasks from the model
        tasks = self.model.get_all_tasks()

        # Display tasks on the calendar
        for task in tasks:
            start_date = datetime.strptime(task.start_date, "%Y-%m-%d")
            self.calendar.calevent_create(start_date, task.task_description, tags=self.task_type_var.get())

        print("Schedule displayed successfully")

    def task_info(self):
        # Get the selected date from the calendar
        selected_date_str = self.calendar.get_date()

        # Convert the selected date to a datetime object
        selected_date = datetime.strptime(selected_date_str, "%m/%d/%y")

        # Get all tasks from the model
        tasks = self.model.get_all_tasks()

        # Check if there are tasks on the selected date
        tasks_on_selected_date = [task for task in tasks if datetime.strptime(task.start_date, "%Y-%m-%d").date() == selected_date.date()]

        if tasks_on_selected_date:
            for task in tasks_on_selected_date:
                # If there's a match, create a new popup window to display task information
                popup = tk.Toplevel(self.root)
                popup.title("Task Information")

                # Display task information in the popup window
                task_info = f"Task Description: {task.task_description}\nTask Type: {task.task_type}\nDate: {task.start_date}\nStart Time: {task.start_time}\nDuration: {task.duration} minutes"
                ttk.Label(popup, text=task_info).pack(padx=10, pady=10)
                print(task_info)
        else:
            messagebox.showinfo("No Tasks", "There are no tasks on the selected date.")

    def run(self):
        # Run the Tkinter main loop
        self.root.mainloop()
