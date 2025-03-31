# Thường thì function attribute sẽ được gán sau khi đã định nghĩa hàm xong

def process_data() -> None:
    """A sample function that simulates processing data.
    """
    print("Processing data...")

# Adding metadata as attributes
process_data.metadata = {"author": "haongnd", "version": "1.0"}       # use case 1: metadata storage 
process_data.description = "A sample function"

print(process_data.metadata)
print(process_data.description)


# Use case 2: custom tags / flags for special handling 
def task_one() -> None:
    print("Taske one running...")

def task_two() -> None:
    print("Task two running...")

# Mark tasks with priority attribute
task_one.priority = 1
task_two.priority = 2

# Sort and execute tasks based on priority
tasks = [task_two, task_one]
for task in sorted(tasks, key=lambda task: task.priority):
    task()


# Built-in attributes of functions
print(process_data.__name__)
print(process_data.__doc__)             # docstring
print(process_data.__annotations__)     # type annotations for function args and return values
print(process_data.__defaults__)        # default args
print(process_data.__kwdefaults__)      # default kwargs
print(process_data.__code__)
