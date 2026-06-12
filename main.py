import argparse
from rich import print

from utils.storage import load_data, save_data

USERS_FILE = "data/users.json"
PROJECTS_FILE = "data/projects.json"
TASKS_FILE = "data/tasks.json"

# ---------------- USERS ----------------
def add_user(args):
    users = load_data(USERS_FILE)

    user = {
        "id": len(users) + 1,
        "name": args.name,
        "email": args.email
    }

    users.append(user)
    save_data(USERS_FILE, users)

    print("[green]User created successfully[/green]")


def list_users(args):
    users = load_data(USERS_FILE)
    print(users)


# ---------------- PROJECTS ----------------
def add_project(args):
    projects = load_data(PROJECTS_FILE)

    project = {
        "id": len(projects) + 1,
        "user": args.user,
        "title": args.title,
        "description": args.description,
        "due_date": args.due_date
    }

    projects.append(project)
    save_data(PROJECTS_FILE, projects)

    print("[blue]Project added successfully[/blue]")


def list_projects(args):
    projects = load_data(PROJECTS_FILE)

    for p in projects:
        if p["user"] == args.user:
            print(p)


# ---------------- TASKS ----------------
def add_task(args):
    tasks = load_data(TASKS_FILE)

    task = {
        "id": len(tasks) + 1,
        "project": args.project,
        "title": args.title,
        "status": "pending"
    }

    tasks.append(task)
    save_data(TASKS_FILE, tasks)

    print("[yellow]Task added[/yellow]")


def complete_task(args):
    tasks = load_data(TASKS_FILE)

    for task in tasks:
        if task["title"] == args.title:
            task["status"] = "completed"

    save_data(TASKS_FILE, tasks)
    print("[green]Task completed[/green]")


def list_tasks(args):
    tasks = load_data(TASKS_FILE)

    for t in tasks:
        if t["project"] == args.project:
            print(t)


# ---------------- CLI SETUP ----------------
def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    # add-user
    p1 = subparsers.add_parser("add-user")
    p1.add_argument("--name", required=True)
    p1.add_argument("--email", required=True)
    p1.set_defaults(func=add_user)

    # list-users
    p2 = subparsers.add_parser("list-users")
    p2.set_defaults(func=list_users)

    # add-project
    p3 = subparsers.add_parser("add-project")
    p3.add_argument("--user", required=True)
    p3.add_argument("--title", required=True)
    p3.add_argument("--description", required=True)
    p3.add_argument("--due_date", required=True)
    p3.set_defaults(func=add_project)

    # list-projects
    p4 = subparsers.add_parser("list-projects")
    p4.add_argument("--user", required=True)
    p4.set_defaults(func=list_projects)

    # add-task
    p5 = subparsers.add_parser("add-task")
    p5.add_argument("--project", required=True)
    p5.add_argument("--title", required=True)
    p5.set_defaults(func=add_task)

    # list-tasks
    p6 = subparsers.add_parser("list-tasks")
    p6.add_argument("--project", required=True)
    p6.set_defaults(func=list_tasks)

    # complete-task
    p7 = subparsers.add_parser("complete-task")
    p7.add_argument("--title", required=True)
    p7.set_defaults(func=complete_task)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()