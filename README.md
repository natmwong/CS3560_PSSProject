# CS3560 Homework 3 & 4 Python

Our group designed a PSS. We have CRC card, Class Diagram, state diagrams, sequence models and activity diagrams design for the system.

## So what is PSS?

PSS helps organize tasks like classes or assignments, creating schedules based on user preferences. Users can view schedules daily, weekly, or monthly, and tasks can be saved or loaded from a file. When adding a task, users specify its type, start time, and duration. PSS alerts if new tasks overlap existing ones. Tasks can be recurring (e.g., weekly classes) or transient (e.g., doctor's appointments), with options for canceling specific occurrences. Recurring tasks include Course, Study, Sleep, Exercise, Work, and Meal. Transient tasks include Visit, Shopping, and Appointment, with room for more types.
## Getting Started

### Design

Our PSS uses the Model-View-Controller pattern, our implementation will have three primary categories of objects: a Model, a
Viewer, and a Controller.
* The Model manages the data, which in this case is the list of all of the tasks. The model can be
asked to return various lists of tasks, and can be asked to create, edit, or delete tasks. The
model makes sure that there are no errors, such as overlapping tasks or tasks that are too large
or too small.
* The Viewer (and you may have multiple objects that are Viewers) are used to display some
information. This is how the user can see a schedule or a part of a schedule.
* The Controller is the main object that interacts with the user. The controller decides what actions to take.
There are other classes as well, such as the hierarchy of tasks supported by the system. 

## Authors

Contributors names

* Daren Sathy 
* John West
* Natasha Wong
* Natalia Jauregui  

## Version History

* 0.2 ~ coming soon 
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release



## Acknowledgments

Followed program outline for CS 3560.01 Object Oriented Design and Programming with Dr. Johannsen at Cal Poly Pomona (Spring 2024)



