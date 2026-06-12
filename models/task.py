class Task:
    id_counter = 1

    def __init__(self, title, project_id, assigned_to=None):
        self.id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.project_id = project_id
        self.assigned_to = assigned_to
        self.status = "pending"

    def mark_complete(self):
        self.status = "completed"

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"