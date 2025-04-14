# File to define Task class

# import dependencies
import time

# creating json file


# build framework for tasks
class Task:
    """Task class"""

    id: int = 0  # task id
    description: str = ""  # short desc of task
    status: str = ""  # done, todo, in progress
    createdAt: str = ""  # time of creation
    updatedAt: str = ""  # time of last update

    def __init__(self):
        self.id: int = 0
        self.description: str = ""
        self.status: str = ""
        self.createdAt: str = time.strftime("%Y%m%d-%H%M%S")
        self.updatedAt: str = ""
        return None

    def update_task(self, userInput: str):
        """
        Task updating function

        Args:
            userInput (str): User's input -- this string will replace the current task description

        Returns:
            None: Modifies the object in place, doesn't need a return value
        """
        self.updatedAt = time.strftime("%Y%m%d-%H%M%S")
        self.description = userInput

        return None
