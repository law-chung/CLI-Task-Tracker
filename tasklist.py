# File to define Task List Class

# 
from .task import Task


# build framework for task list
class TaskList:
    taskList: list[Task]
    doneTasks = list[Task]
    todoTasks = list[Task]
    inProgressTasks = list[Task]

    def __init__(self):
        self.taskList: list[Task] = []
        self.doneTasks: list[Task] = []
        self.todoTasks: list[Task] = []
        self.inProgressTasks: list[Task] = []

    def check_done_tasks(self):
        for task in self.taskList:
            if task.status == "done":
                self.doneTasks += task

        return self.doneTasks

    def check_todo_tasks(self):
        for task in self.taskList:
            if task.status == "todo":
                self.todoTasks += task

        return self.todoTasks

    def check_in_progress_tasks(self):
        for task in self.taskList:
            if task.status == "in progress":
                self.inProgressTasks += task

        return self.inProgressTasks

    def add_task(self, task: Task):
        """
        Add a task to the task list

        Args:
            task (Task): Task object to be added

        Returns:
            None: Modifies the object in place, doesn't need a return value
        """
        
        self.taskList.append(task)
        return None

    def delete_task(self, task: Task):
        self.taskList.pop(Task)
        return None
