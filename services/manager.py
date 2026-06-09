from models.user import User
from models.project import Project
from models.task import Task
from services.storage import load_data, save_data


class Manager:

    def __init__(self):
        self.data = load_data()
        self.users = []

    def create_user(self, name, email):
        user = User(name, email)
        self.users.append(user)
        return user

    def find_user(self, name):
        for u in self.users:
            if u.name == name:
                return u
        return None

    def add_project(self, username, title):
        user = self.find_user(username)
        if not user:
            return None

        project = Project(title)
        user.add_project(project)
        return project

    def add_task(self, project_title, task_title):
        for user in self.users:
            for project in user.projects:
                if project.title == project_title:
                    task = Task(task_title)
                    project.add_task(task)
                    return task
        return None

    def save(self):
        data = {"users": []}

        for u in self.users:
            data["users"].append({
                "name": u.name,
                "email": u.email,
                "projects": [
                    {
                        "title": p.title,
                        "tasks": [t.title for t in p.tasks]
                    } for p in u.projects
                ]
            })

        save_data(data)