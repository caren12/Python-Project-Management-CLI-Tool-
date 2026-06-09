import argparse
from services.manager import Manager
from rich import print

manager = Manager()

parser = argparse.ArgumentParser(description="Project Management CLI")

subparsers = parser.add_subparsers(dest="command")


# ADD USER
add_user = subparsers.add_parser("add-user")
add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)


# ADD PROJECT
add_project = subparsers.add_parser("add-project")
add_project.add_argument("--user", required=True)
add_project.add_argument("--title", required=True)


# ADD TASK
add_task = subparsers.add_parser("add-task")
add_task.add_argument("--project", required=True)
add_task.add_argument("--title", required=True)


# LIST USERS
list_users = subparsers.add_parser("list-users")


args = parser.parse_args()


if args.command == "add-user":
    user = manager.create_user(args.name, args.email)
    print(f"[green]Created user:[/green] {user}")

elif args.command == "add-project":
    project = manager.add_project(args.user, args.title)
    print(project or "User not found")

elif args.command == "add-task":
    task = manager.add_task(args.project, args.title)
    print(task or "Project not found")

elif args.command == "list-users":
    for u in manager.users:
        print(u)

manager.save()