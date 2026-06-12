import click
from rich import print

from utils.storage import load_data, save_data

USERS_FILE = "data/users.json"
PROJECTS_FILE = "data/projects.json"
TASKS_FILE = "data/tasks.json"


# ---------------- CLI GROUP ----------------
@click.group()
def cli():
    pass


# ---------------- USERS ----------------
@cli.command()
@click.option("--name", required=True)
@click.option("--email", required=True)
def add_user(name, email):
    users = load_data(USERS_FILE)

    user = {
        "id": len(users) + 1,
        "name": name,
        "email": email
    }

    users.append(user)
    save_data(USERS_FILE, users)

    print("[green]User created successfully[/green]")


@cli.command()
def list_users():
    users = load_data(USERS_FILE)
    print(users)


# ---------------- PROJECTS ----------------
@cli.command()
@click.option("--user", required=True)
@click.option("--title", required=True)
@click.option("--description", required=True)
@click.option("--due_date", required=True)
def add_project(user, title, description, due_date):
    projects = load_data(PROJECTS_FILE)

    project = {
        "id": len(projects) + 1,
        "user": user,
        "title": title,
        "description": description,
        "due_date": due_date
    }

    projects.append(project)
    save_data(PROJECTS_FILE, projects)

    print("[blue]Project added successfully[/blue]")


@cli.command()
@click.option("--user", required=True)
def list_projects(user):
    projects = load_data(PROJECTS_FILE)

    for p in projects:
        if p["user"] == user:
            print(p)


# ---------------- TASKS ----------------
@cli.command()
@click.option("--project", required=True)
@click.option("--title", required=True)
def add_task(project, title):
    tasks = load_data(TASKS_FILE)

    task = {
        "id": len(tasks) + 1,
        "project": project,
        "title": title,
        "status": "pending"
    }

    tasks.append(task)
    save_data(TASKS_FILE, tasks)

    print("[yellow]Task added[/yellow]")


@cli.command()
@click.option("--project", required=True)
def list_tasks(project):
    tasks = load_data(TASKS_FILE)

    for t in tasks:
        if t["project"] == project:
            print(t)


@cli.command()
@click.option("--title", required=True)
def complete_task(title):
    tasks = load_data(TASKS_FILE)

    for task in tasks:
        if task["title"] == title:
            task["status"] = "completed"

    save_data(TASKS_FILE, tasks)

    print("[green]Task completed[/green]")


# ---------------- DELETE TASK (you wanted this earlier) ----------------
@cli.command()
@click.option("--id", type=int, required=True)
def delete_task(id):
    tasks = load_data(TASKS_FILE)

    new_tasks = [t for t in tasks if t["id"] != id]

    if len(new_tasks) == len(tasks):
        print(f"[red]Task with id {id} not found[/red]")
        return

    save_data(TASKS_FILE, new_tasks)

    print(f"[red]Task {id} deleted successfully[/red]")


# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    cli()