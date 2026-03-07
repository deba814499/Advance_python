class ToDoManager:

    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Task title: ")
        category = input("Category: ")
        priority = int(input("Priority (1-High,2-Medium,3-Low): "))
        deadline = input("Deadline: ")

        task = {
            "title": title,
            "category": category,
            "priority": priority,
            "deadline": deadline,
            "status": "Pending"
        }

        self.tasks.append(task)

    def view_tasks(self):
        for i, t in enumerate(self.tasks):
            print(i+1, t)

    def mark_completed(self):
        num = int(input("Enter task number: "))
        self.tasks[num-1]["status"] = "Completed"


t = ToDoManager()

while True:
    print("\nToDo Manager")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Mark Completed")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        t.add_task()
    elif ch == 2:
        t.view_tasks()
    elif ch == 3:
        t.mark_completed()
    elif ch == 4:
        break