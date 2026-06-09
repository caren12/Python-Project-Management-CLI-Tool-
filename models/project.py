class Project:
    id_counter = 1

    def __init__(self, title, description="", due_date=None):
        self.id = Project.id_counter
        Project.id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __repr__(self):
        return f"Project(title={self.title}, tasks={len(self.tasks)})"