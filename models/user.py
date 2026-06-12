class User:
    id_counter = 1

    def __init__(self, name, email):
        self.id = User.id_counter
        User.id_counter += 1

        self.name = name
        self.email = email
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"