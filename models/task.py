class Task:
    id_counter = 1

    def __init__(self, title, assigned_to=None):
        self.id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.status = "pending"
        self.assigned_to = assigned_to

    def mark_complete(self):
        self.status = "completed"

    def __repr__(self):
        return f"Task(title={self.title}, status={self.status})"