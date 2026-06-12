Project Management CLI Tool (Clinic System)
What this project is

This is a simple computer program that helps you manage clinic or project work using text commands.

Instead of clicking buttons in a website or app, you type commands in the terminal (a text-based window on your computer).

It helps you:

Add users (for example: staff or system users)
Create projects (for example: a clinic system or department work)
Add tasks (things that need to be done)
Track and complete tasks
Delete tasks when they are no longer needed

All information is saved on your computer in simple files.

Who this is for

This project is useful for:

Students learning programming
Beginners practicing Python
Anyone learning how real systems manage data
People interested in clinic or task management systems
How it works (simple explanation)

Think of it like a notebook:

Users are written in one notebook
Projects are written in another notebook
Tasks are written in another notebook

Instead of writing by hand, the program writes and updates everything automatically.

When you type a command, the program:

Reads the data file
Updates it
Saves it back
Features

You can do the following:

1. Manage users
Add a new user
View all users
2. Manage projects
Create a project
View projects linked to a user
3. Manage tasks
Add tasks under a project
View tasks in a project
Mark tasks as complete
Delete tasks by ID
What you need before using it

You need:

A computer
Python installed
Basic ability to open a terminal (command window)
Project structure (what files are inside)
project/
│
├── main.py                # The main program you run
├── utils/
│   └── storage.py         # Handles saving and loading data
│
├── data/
│   ├── users.json         # Stores user information
│   ├── projects.json      # Stores project information
│   └── tasks.json         # Stores task information
How to install and run
Step 1: Install required tools

Open your terminal and run:

pip install click rich
Step 2: Go to the project folder
cd project
Step 3: Run the program
python main.py
How to use the system

You type commands like instructions.

USER MANAGEMENT
Add a user

This creates a new person in the system.

python main.py add-user --name "John Doe" --email "john@example.com"
View all users
python main.py list-users
PROJECT MANAGEMENT
Add a project

A project is like a big task (example: Clinic System).

python main.py add-project --user "John Doe" --title "Clinic System" --description "Hospital management system" --due_date "2026-01-01"
View projects for a user
python main.py list-projects --user "John Doe"
TASK MANAGEMENT
Add a task

A task is a small job inside a project.

python main.py add-task --project "Clinic System" --title "Register Patients"
View tasks
python main.py list-tasks --project "Clinic System"
Mark task as completed
python main.py complete-task --title "Register Patients"
Delete a task

If a task is no longer needed:

python main.py delete-task --id 2
What happens when you run a command

When you type a command:

The program opens the data file
Finds the correct information
Updates or adds new data
Saves everything automatically

You do NOT need to edit files manually.

Where your data is stored

All your information is stored in these files:

users.json → stores users
projects.json → stores projects
tasks.json → stores tasks

These files act like digital notebooks.

Important notes
Each item (user, project, task) has a unique ID number
IDs help the system find and delete items correctly
If a file is empty or deleted, data will reset
Everything runs locally on your computer
Limitations

This is a learning project, so:

It does not use a database
It does not have login or security
It does not support multiple users online
Data is stored only on one computer
Future improvements

This system can be improved to:

Add real database storage (like SQLite)
Add login system for clinic staff
Replace users with patients and doctors
Add appointment scheduling
Add search functionality
Turn it into a real clinic management system