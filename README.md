Project Management CLI Tool (Click-Based)

A command-line application built with Python Click for managing users, projects, and tasks.
This tool simulates a basic clinic or project management system using JSON file storage.

Features
User management (add, list users)
Project management (add, list projects)
Task management (add, list, complete, delete tasks)
JSON file-based storage (no database required)
Fast CLI experience using Click
Tech Stack
Python 3
Click (CLI framework)
Rich (for terminal output styling)
JSON (data storage)
Project Structure
project/
│
├── main.py
├── utils/
│   └── storage.py
│
├── data/
│   ├── users.json
│   ├── projects.json
│   └── tasks.json
│
└── README.md
Installation
1. Clone the project
git clone <your-repo-url>
cd project
2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install dependencies
pip install click rich
Running the CLI
python main.py
Available Commands
Users
Add user
python main.py add-user --name "John Doe" --email "john@example.com"
List users
python main.py list-users
Projects
Add project
python main.py add-project --user "John Doe" --title "Clinic System" --description "Hospital management system" --due_date "2026-01-01"
List projects
python main.py list-projects --user "John Doe"
Tasks
Add task
python main.py add-task --project "Clinic System" --title "Register Patients"
List tasks
python main.py list-tasks --project "Clinic System"
Complete task
python main.py complete-task --title "Register Patients"
Delete task
python main.py delete-task --id 2
Data Storage

All data is stored locally in JSON files:

data/users.json
data/projects.json
data/tasks.json

Files are automatically updated when commands run.

Design Notes
Click is used for CLI command handling
Each entity (users, projects, tasks) is stored separately
IDs are generated using list length
Lightweight file-based architecture
Limitations
No authentication system
No database (JSON only)
IDs may reset if files are cleared or reordered
No concurrency handling
Future Improvements
Add SQLite database support
Add authentication for clinic staff
Replace users with patients and doctors
Add appointment scheduling system
Improve ID generation using UUIDs
Add search and filtering commands
Author

Python CLI project for learning Click, CLI design, and file-based data storage.